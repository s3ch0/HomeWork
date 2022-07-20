SQL_CMD = {
    'species_data':
    "select species,count(*) as num from cell group by species;",
    'grade_data':
    "select grade,count(*) from cell group by grade;",
    'length_data_':
    "select shaft_length,count(*) from detail group by shaft_length order by count(*) desc limit 10;",
    'time_data_':
    "select time,count(*) from detail where time not like 'Null' group by time;",
    'species_data_':
    "select species,count(*) from detail group by species order by count(*) desc limit 6;",
    'tough_data_':
    "select tube_toughness , count(*) from detail group by tube_toughness order by count(*) desc limit 6;"

}

