# XBRL Taxonomy Counts

Someone asked me if there was comprehensive list of tags used in SEC financials. To my knowledge, no. So here is a repository to fix that.

Data is in simple_xbrl_taxonomy_counts/. Every SEC XBRL taxonomy name since the program began in 2004.


Code to construct data. Uses [datamule's](https://datamule.xyz/articles/datamule-xbrl) api.

```python
from datamulehub import databases

databases.query(
    "SELECT name, COUNT(*) AS count FROM simple_xbrl GROUP BY name ORDER BY count DESC",
    output_dir="simple_xbrl_name_counts",
)
```

Code to construct data for specific industry, by SIC code.

```python
from datamulehub import databases

databases.query(
    """
    SELECT x.name, COUNT(*) AS count
    FROM simple_xbrl x
    WHERE EXISTS (
        SELECT 1
        FROM sec_accession_cik_table c
        JOIN filer_metadata f ON f.cik = c.cik
        WHERE c.accessionnumber = x.accessionnumber
          AND f.sic = '7372'
    )
    GROUP BY x.name
    ORDER BY count DESC
    """,
    output_dir="simple_xbrl_name_counts_sic_7372",
)
```



