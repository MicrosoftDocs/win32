---
description: Because the upgrade updates the files used by the application, you must modify the File table of the database.
ms.assetid: 65a7ae86-b426-4dd4-8cf5-f905dc2a1727
title: Updating Files and File Attributes for an Upgrade
ms.topic: article
ms.date: 05/31/2018
---

# Updating Files and File Attributes for an Upgrade

Because the upgrade updates the files used by the application, you must modify the [File table](file-table.md) of the database. Use the database editor Orca that is provided with the SDK, or another editor to open MNP2001.msi and enter the following data into the [File table](file-table.md).

[File Table](file-table.md)



| File         | Component\_ | FileName     | FileSize | Version | Language | Attributes | Sequence |
|--------------|-------------|--------------|----------|---------|----------|------------|----------|
| Baseba01.txt | Baseball    | Baseba01.txt | 1000     |         |          | 0          | 1        |
| Concer01.txt | Concert     | Concer01.txt | 1000     |         |          | 0          | 1        |
| Dance01.txt  | Dance       | Dance01.txt  | 1000     |         |          | 0          | 1        |
| Opera01.txt  | Opera       | Opera01.txt  | 1000     |         |          | 0          | 1        |
| Footba01.txt | Football    | Footba01.txt | 1000     |         |          | 0          | 1        |
| Basket01.txt | Basketball  | Basket01.txt | 1000     |         |          | 0          | 1        |
| Help.txt     | Help        | Help.txt     | 1000     |         |          | 0          | 1        |
| Januar01.txt | January     | Januar01.txt | 1000     |         |          | 0          | 1        |
| NewYea01.txt | NewYears    | NewYea01.txt | 1000     |         |          | 0          | 1        |
| Memori01.txt | Memorial    | Memori01.txt | 1000     |         |          | 0          | 1        |
| Redpark.exe  | Notepad     | Redpark.exe  | 45328    |         |          | 0          | 1        |
| Readme.txt   | Notepad     | Readme.txt   | 1000     |         |          | 0          | 1        |



 

[Continue](updating-components-for-an-upgrade.md)

 

 



