---
Description: 'System administrators or users should routinely backup the RSM database. For instructions on how to do this, see the Resource Kit.'
ms.assetid: '3de26b2c-382c-4f0c-ae97-515e1fac0e53'
title: Recovering from a Disaster
---

# Recovering from a Disaster

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

System administrators or users should routinely backup the RSM database. For instructions on how to do this, see the Resource Kit.

If you are writing a backup application that is used to backup system databases such as RSMs, or if your application requires its own preparations for disaster recovery that might require special handling of the RSM database, then you need to call specific RSM functions in order to get a consistent copy of the database files. For example, Remote Storage makes copies of the RSM database files at the end of each data migration job. In a disaster situation, it is possible to completely restore Remote Storage even if the administrator has not been routinely backing up RSM's database explicitly.

## Backing Up the RSM Database

The default location of the RSM database is %SYSTEMROOT%\\System32\\NTMSData. The actual location of the database can be changed to any location. The current location of the database is found in the registry under

**HKLM\\System\\CurrentControlSet\\Control\\NTMS**

as the value **NtmsData**. The database files are always stored in a folder named **NtmsData** under the folder given in this value. If RSM is not running, it is a sufficient backup strategy is to make copies of these files. Most backup applications, though, require RSM to be running while the backup occurs.

To back up the RSM database while RSM is running, an application must open an RSM session and use the [**ExportNtmsDatabase**](exportntmsdatabase.md) function. This function creates a consistent replica of the current database. RSM creates the replica in the Export subdirectory of the RSM database directory.

## Recovering the Database

When the RSM database files have been restored from a backup two additional step are needed before RSM will begin using the restored database. First the recovery application must call the [**ImportNtmsDatabase**](importntmsdatabase.md) function. This function makes the changes necessary for RSM to import the restored on the next restart. Once this is completed, the next time RSM starts it uses the restored database. This can either be done by restarting the service with the Service Control Manager or rebooting.

## Updating the Restored Database

The database as restored may not have been current at the time of the destructive event. An application may have allocated a tape between the last database backup and a disaster that destroyed the running database.

In general, your application should scan its own pools as well as the free and import pools after a recovery, searching for the OMIDs of its media and any media that may be in the wrong place. The following table describes how your application can resolve each problem.



| Problem                                                                                                                                                                                                                                           | Solution                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| A specified side is deallocated by an application after the backup but before the disaster and remains in the application media pool. RSM recognizes this side as still allocated after the recovery and leaves it in the application media pool. | The application must deallocate this side again.                 |
| A specified side is allocated by an application after the backup but before the disaster. RSM leaves the cartridge in the import or free media pools.                                                                                             | The application can import the cartridge to the free media pool. |



 

## Restoring the RSM Database in the Absence of a Backup

This section describes a strategy for an application to recover the RSM database when the database has been lost and there is no backup copy, but the application has not lost the database that refers to the lost RSM database. For this example it is assumed that the application has kept both the RSM LMID and its own OMID information in its database. An application can take the following steps to in essence create a usable new RSM database:

1.  When RSM starts without a database it does a full inventory and all the media in the library appear in the import pool.
2.  The application must create its media pool(s).

    The application must have a mechanism that scans the Import media pool for its media. This can be accomplished by reading the OMID information of the sides of the physical media and finding all media with the *szOmidLabelType* parameter that is the application's type. As an additional check the application can verify that the *szOmidLabelInfo* parameter is correct for the media.

3.  For all sides found, the application must call the [**AllocateNtmsMedia**](allocatentmsmedia.md) function, specifying the side and media pool.
4.  The application database must be updated with the new LMID that is assigned to the media. The application should search through its database for all cases of the OMID it has found and replace the corresponding LMID with the new one.
5.  Media that were offline and not in the library at the time of the full inventory must be injected into the library so they can be identified and placed in the import pool. To do so, repeat steps 3, 4 and 5.

 

 



