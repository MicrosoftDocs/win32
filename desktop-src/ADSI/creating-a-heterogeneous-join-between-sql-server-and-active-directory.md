---
title: Creating a Heterogeneous Join between SQL Server & Active Directory
description: All employees at the Fabrikam corporation are reviewed every six months.
ms.assetid: 16f605ae-7f6c-4429-a379-47686618b15d
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Heterogeneous Join between SQL Server & Active Directory

All employees at the Fabrikam corporation are reviewed every six months. Review ratings are stored in the Human Resource database in SQL Server. To create a view of this data, Joe Worden, the enterprise administrator, must first create an employee performance review table.

In the SQL Query Analyzer, Joe is going to create a table called EMP\_REVIEW that will contain three columns to hold the name of the employee, the date of the review, and the rating that the employee received.


```sql
CREATE TABLE EMP_REVIEW
(
userName varChar(40),
reviewDate datetime,
rating decimal 
)
```



Joe can then insert a few records.


```sql
INSERT EMP_REVIEW VALUES('Julie Adam', '2/15/1999', 4 )
INSERT EMP_REVIEW VALUES('Julie Bankert', '7/15/1999', 5 )
INSERT EMP_REVIEW VALUES('Chris Gray', '2/15/1999', 3 )
INSERT EMP_REVIEW VALUES('Chris Gray', '7/15/1999', 4 )
```



Now Joe can join the Active Directory user objects to the SQL Server table.

In this example, the [SELECT](https://msdn.microsoft.com/library/Aa259187.aspx) statement contains the list of data that will be obtained from the directory service and SQL Server. The [FROM](https://msdn.microsoft.com/library/Aa258869.aspx) statement contains the name of the linked directory server where this information will be obtained from, in this case, viewADUsers. The [WHERE](https://msdn.microsoft.com/library/Aa260674.aspx) statement provides the search conditions. In this example, it is searching by the name in the directory service, which is set to the SQL userName entered in the previous task.


```sql
SELECT ADsPath, userName, title, ReviewDate, Rating 
FROM EMP_REVIEW, viewADUsers
WHERE userName = Name
```



The previous command gets the result from both SQL Server and Active Directory. AdsPath and title are from Active Directory, whereas userName, ReviewDate, and Rating are from the SQL table. He can even create another view for this join.


```sql
CREATE VIEW reviewReport
AS
SELECT ADsPath, userName, title, ReviewDate, Rating 
FROM EMP_REVIEW, viewADUsers
WHERE userName = Name
GO
SELECT * FROM reviewReport
```



 

 




