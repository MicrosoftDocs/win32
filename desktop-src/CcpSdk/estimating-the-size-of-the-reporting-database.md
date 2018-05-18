---
Description: 'You may need to estimate the current or potential size of the reporting database for your HPC cluster as part of capacity planning for your HPC cluster or if you want to host a copy of the reporting database outside of the HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9f32dc7a-2116-49d4-8fd8-13d0b049d016'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Estimating the Size of the Reporting Database
---

# Estimating the Size of the Reporting Database

You may need to estimate the current or potential size of the reporting database for your HPC cluster as part of capacity planning for your HPC cluster or if you want to host a copy of the reporting database outside of the HPC cluster. This topic provides information about how to estimate the size of the reporting database.

## Factors that affect the size of the reporting database

The size of the reporting database depends mainly on the following factors:

-   The number of jobs for which the database maintains history

-   The average number of cores allocated to those jobs when they run

These factors affect the sizes of the JobHistory and AllocationHistory tables in the reporting database, and these tables have the largest effect on the overall size of the database.

> [!Note]  
> The initial reporting database available immediately after you install Windows HPC Server 2008 R2 includes 128 megabytes (MB) of database and 64 megabytes for log files.

 

You can use the following equations to obtain a rough estimate of the size of the JobHistory and AllocationHistory tables and the overall size of the database:

-   *Approximate\_size\_of\_the\_JobHistory\_table* = *Number\_of\_jobs* × 250 bytes

-   *Approximate\_size\_of\_the\_AllocationHistory\_table* = *Number\_of\_jobs* × *Average\_number\_of\_cores\_allocated\_per\_job* × 136 bytes

-   *Approximate\_size\_of\_the\_reporting\_database* = *Approximate\_size\_of\_the\_JobHistory\_table* + *Approximate\_size\_of\_the\_AllocationHistory\_table*

For example, if your HPC cluster has 10,000 jobs and allocates 100 cores per job on average, the approximate overall size of the database is 140 megabytes.

To get the current size of the reporting database, run the following cmdlet in an **HPC PowerShell** window:

**Get-HpcClusterProperty -Parameter -Name ReportingDBSize**

 

 



