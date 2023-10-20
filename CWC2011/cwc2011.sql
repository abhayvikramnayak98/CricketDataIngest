-- Creating database
CREATE DATABASE CricketDB;
USE CricketDB;

-- Creating table
CREATE TABLE IF NOT EXISTS CWC2011Stats (
    team1 VARCHAR(20),
    team2 VARCHAR(20),
    winner VARCHAR(20),
    margin VARCHAR(20),
    ground VARCHAR(50),
    venue VARCHAR(20)
);

-- Import the data from the given CSV file to SQL database using Data Import Wizard. After importing data, check whether all the data has been imported or not.
select * from CWC2011Stats LIMIT 5;

-- Now creating points table
with
team1_rec as (select 
	team1 as team, 
	count(*) as total, 
	sum(case when team1 = winner then 1 else 0 end) as wins, 
    sum(case when winner = 'NR' then 1 else 0 end) as nr
from
cricketdb.cwc2011stats
group by team1),
team2_rec as (select 
	team2 as team, 
	count(*) as total, 
	sum(case when team2 = winner then 1 else 0 end) as wins, 
    sum(case when winner = 'NR' then 1 else 0 end) as nr
from
cricketdb.cwc2011stats
group by team2),
total_matches as (select * from team1_rec union all select * from team2_rec),
allMatchStats as (select team, sum(total) as total, sum(wins) as wins, sum(nr) as nr from total_matches group by team)
select *, total-wins-nr as loss, (wins*2)+nr as pts from allMatchStats order by pts desc;
