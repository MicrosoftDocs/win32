---
title: Backing Up and Restoring the Failover Cluster Configuration with Windows Server 2003
description: Starting with Windows Server 2008, you can back up and restore the failover cluster configuration with the Volume Shadow Copy Service (VSS). For information, see Backing Up and Restoring the Failover Cluster Configuration Using VSS.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a8914274-7cbc-4f10-9611-f625994f14c8
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- backing up the cluster configuration Failover Cluster
- restoring the cluster configuration Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Backing Up and Restoring the Failover Cluster Configuration with Windows Server 2003

Starting with Windows Server 2008, you can back up and restore the failover cluster configuration with the Volume Shadow Copy Service (VSS). For information, see [Backing Up and Restoring the Failover Cluster Configuration Using VSS](backing-up-and-restoring-the-failover-cluster-configuration-using-vss.md).

Failover clustering did not support VSS before Windows Server 2008. The following example shows how to back up and restore the failover cluster configuration in systems prior to Windows Server 2008.

Before changing the cluster configuration, you can create a backup of the [cluster database](cluster-database.md) using the [Cluster API](cluster-api.md) function [**BackupClusterDatabase**](/windows/previous-versions/ClusAPI/nf-clusapi-backupclusterdatabase?branch=master). This creates a snapshot of the cluster configuration which can later be restored with the [**RestoreClusterDatabase**](/windows/previous-versions/ClusAPI/nf-clusapi-restoreclusterdatabase?branch=master) function.

The following example is a command-line tool that performs basic backup and restore operations.


```C++
//////////////////////////////////////////////////////////////////////
/*

CLUBAR.CPP

Cluster database backup and restore example demonstrating the
BackupClusterDatabase and RestoreClusterDatabase functions. 

To use this example, compile with the ClusDocEx.h header file, then run 
it using the following command-line syntax:

  Back up:    clubar b[ackup] {cluster name} {backup path}
  Restore**:  clubar r[estore] {backup path} {[no]force} [{drive}]

** USE WITH CAUTION. This operation will replace the existing cluster
   database with the specified backup.

*/
//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////


//--------------------------------------------------------------------
//  ShowHelp
//  Displays command-line syntax.
//--------------------------------------------------------------------
void ShowHelp()
 {
  wprintf( L"\n\nCLUBAR\n" );
  wprintf( L"===========\n" );
  wprintf( L"Demonstration of BackupClusterDatabase and RestoreClusterDatabase.\n\n" );
  wprintf( L"Command-line syntax:\n\n" );
  wprintf( L"     argv[0] argv[1]   argv[2]        argv[3]       arg[4]\n" );
  wprintf( L"     clubar  b[ackup]  {cluster name} {backup path}\n" );
  wprintf( L"     clubar  r[estore] {backup path}  {[no]force}   [{drive letter}]\n\n" );
  wprintf( L"     [] denotes optional syntax\n" );
  wprintf( L"     {} denotes user-supplied value\n\n" );
  wprintf( L"Examples:\n" );
  wprintf( L"     clubar b MY_CLUSTER_NAME d:\\backups\\19990415\n" );
  wprintf( L"     clubar r d:\\backups\\19990415 force k:\n" );
  wprintf( L"     clubar restore a:\\ noforce\n" );
 }
//  end ShowHelp
//--------------------------------------------------------------------


int main( int argc, char *argv[] )
{
  HCLUSTER hCluster = NULL;    

  WCHAR szClusterName[ClusDocEx_DEFAULT_CB];
  WCHAR szPath[ClusDocEx_DEFAULT_CB];
  WCHAR szOperation[ClusDocEx_DEFAULT_CB];

  WCHAR szDriveLetter[ClusDocEx_DEFAULT_CB];
  BOOL  bForce = FALSE;

  DWORD dwResult = ERROR_SUCCESS;

  if( argc < 4 )
    goto error_end;
    

  if( toupper( *argv[1] ) == 'R' )
   {    
    //  Argument 2 should be path.

    if( ( dwResult = ConvertArg( argv[2], szPath, ClusDocEx_DEFAULT_CB ) ) != ERROR_SUCCESS )
      goto error_end;

    //  Argument 3 is the force option.

    if( strcmpi( argv[3], "force" ) == 0 )
      bForce = TRUE;

    if( argc > 4 )
     {
      if( ( dwResult = ConvertArg( argv[4], szDriveLetter, ClusDocEx_DEFAULT_CB ) ) != ERROR_SUCCESS )
        goto error_end;

      //  Use only the first two characters.
      //  Optionally add syntax check here to make sure
      //  first character is alphabetic and second character is a colon.
      szDriveLetter[2] = L'\0';
     }

    // Validate path.
    if( !ResUtilIsPathValid( szPath ) )
     {
      wprintf( L"The specified target path is invalid." );
      goto error_end;
     }

    wprintf( L"\n\n**** WARNING!!! ****\n\n"
             L"The existing cluster database will be replaced by the backup stored in %s. "
             L"If you are sure you want to proceed, enter 'y'. Enter any other key to cancel.\n"
             L"Proceed (y/n):  ", szPath );
    if( towupper( getwc(stdin) ) != L'Y' )
      goto error_end;

    //  Restore
    if( argc < 4 )
      dwResult = RestoreClusterDatabase( szPath, bForce, NULL );
    else
      dwResult = RestoreClusterDatabase( szPath, bForce, szDriveLetter );

        
    switch( dwResult )
     {
      case ERROR_CLUSTER_NODE_UP:
        wprintf( L"\n\nERROR: ACTIVE CLUSTER NODES\n" );
        wprintf( L"Other cluster nodes are currently active. " );
        wprintf( L"Only the node used perform the restore can be running the Cluster service.\n" );
        wprintf( L"\nOptions:\n" );
        wprintf( L"(1) Manually shut down the Cluster service on all the other nodes.\n" );
        wprintf( L"(2) Run the program again using the FORCE command-line argument. \n" );
        wprintf( L"The restore routine will attempt to shut down the Cluster service on all other nodes.\n" );
        break;

      case ERROR_QUORUM_DISK_NOT_FOUND:
        wprintf( L"\n\nERROR: QUORUM DISK NOT FOUND\n" );
        wprintf( L"The restore routine cannot find a quorum disk with the same partition layout as \n"
                 L"the quorum disk described in the backup. The existing quorum disk must have a layout \n"
                 L"(number of partitions and offsets to each partition) identical to the layout stored \n"
                 L"in the backup.\n" );
        wprintf( L"\nOptions.\n" );
        wprintf( L"(1) Manually reconfigure the quorum disk to match the layout described in the backup.\n" );
        wprintf( L"(2) Run the program again using the FORCE command-line argument. The restore routine \n"
                 L"    will attempt to reconfigure the quorum disk to match the disk described in the backup.\n" );
        break;

      case ERROR_SUCCESS:
        wprintf( L"\n\nSUCCESS\n" );
        wprintf( L"The restore routine succeeded.  Start the Cluster service on the other cluster nodes to "
                 L"complete the restore operation.  As nodes join the cluster, they will update their cluster "
                 L"databases to match the restored configuration." );        
        break;
      default:
        ClusDocEx_DebugPrint( L"RestoreClusterDatabase failed", dwResult );
        break;
     }
   }

  else if( toupper( *argv[1] ) == 'B' )
   {
    //  BACKUP

    //  Argument 2 should be cluster name.

    if( ( dwResult = ConvertArg( argv[2], szClusterName, ClusDocEx_DEFAULT_CB ) ) != ERROR_SUCCESS )
      goto error_end;

    //  Argument 3 should be path.

    if( ( dwResult = ConvertArg( argv[3], szPath, ClusDocEx_DEFAULT_CB ) ) != ERROR_SUCCESS )
      goto error_end;

    //  Validate path.

    if( !ResUtilIsPathValid( szPath ) )
     {
      ClusDocEx_DebugPrint( L"The specified target path is invalid.", 0 );
      goto error_end;
     }

     //  Get cluster handle.

     hCluster = OpenCluster( szClusterName );
     if( hCluster == NULL )
      {
       ClusDocEx_DebugPrint( L"Unable to open a handle to the specified cluster", GetLastError() );
       goto error_end;
      }

     //  Perform backup.

     dwResult = BackupClusterDatabase( hCluster, szPath );

     if( dwResult != ERROR_SUCCESS )
      {
       ClusDocEx_DebugPrint( L"BackupClusterDatabase call failed", GetLastError() );
       goto error_end;
      }

     wprintf( L"\nDone. The cluster database has been backed up to %s. The backup consists of the following files:\n"
              L"    chk????.tmp\n    quolog.log\n    *.cpt\n    *.cpr\n\n", szPath );

   }       //  end BACKUP

  else
   {
    //  Bad syntax

    ShowHelp();
    goto error_end;
   }
    
error_end:

  if( hCluster != NULL )
    CloseCluster( hCluster );

  if( dwResult )
    return 1;
  else
    return 0;

}
```



 

 




