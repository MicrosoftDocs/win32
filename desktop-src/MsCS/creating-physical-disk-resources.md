---
title: Creating Physical Disk Resources
description: Applications may need to obtain access to a disk on a shared bus in order to secure data storage or satisfy dependency requirements for a resource. To make a disk usable as a cluster resource, create a Physical Disk resource for it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 003bc879-d526-4f7d-8f58-a9002f78819d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resources Failover Cluster ,creating,Physical Disk
- Physical Disk resource type Failover Cluster ,resources,creating
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Physical Disk Resources

Applications may need to obtain access to a disk on a shared bus in order to secure data storage or satisfy [dependency](resource-dependencies.md) requirements for a [resource](resources.md). To make a disk usable as a [*cluster*](https://www.bing.com/search?q=*cluster*) resource, create a [*Physical Disk resource*](https://www.bing.com/search?q=*Physical Disk resource*) for it.

New Physical Disk resources should be created only for available [*cluster-capable disks*](https://www.bing.com/search?q=*cluster-capable disks*). That is, disks that are accessible by all cluster nodes and that are not associated with an existing Physical Disk resource.

Note that the Physical Disk resources cannot be created for partitions or logical drives, only entire physical drives. There is currently no way to independently [fail over](failover.md) drive partitions on the same disk. A Physical Disk resource can be created for a partitioned drive, but the resource is associated with the entire disk, partitions and all.

**To Create a Physical Disk Resource**

1.  Determine search criteria for selecting a disk. Refer to [**CLUSPROP\_PARTITION\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_partition_info) and [**CLUSPROP\_PARTITION\_INFO\_EX**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_partition_info_ex) for the kinds of data that can be searched for.
2.  Create or select a [group](groups.md) in which to create the new resource (see [**CreateClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_group) and [**OpenClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_group).)
3.  Get a list of available disks. Call [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) with the [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS](clusctl-resource-type-storage-get-available-disks.md) or [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX](clusctl-resource-type-storage-get-available-disks-ex.md) control code.
4.  Parse the resulting [value list](value-lists.md) for a disk matching the criteria determined in step 1. (See [Parsing a Value List](parsing-a-value-list.md).) If a disk is found:

    -   Get the signature or **GUID** of the disk.
    -   Get the drive letters of all partitions of the disk.

5.  Create a resource by calling [**CreateClusterResource**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_resource), specifying "Physical Disk" as the [resource type](resource-types.md).
6.  Set the new resource's [**DiskSignature**](disksignature.md) or [**DiskIdGuid**](diskidguid.md) private property to the signature or **GUID** obtained in step 4. You must set one or the other of these properties, but not both. Do not change either property after this assignment is made.

Once created, the Physical Disk resource can be brought online, used as a dependency, or otherwise controlled with the [Resource Management Functions](resource-management-functions.md). It will appear as a cluster resource in failover cluster cmdlet reporting commands.

**Windows Server 2008:** The Physical Disk resource appears as a cluster resource in [Cluster.exe](cluster-exe.md).

## Example Code

The following example creates a Physical Disk resource for a disk identified by drive letter.


```C++
//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESCREATEDISK_CPP
#define _CLUSDOCEX_RESCREATEDISK_CPP
//--------------------------------------------------------------------
//
// ClusDocEx_ResCreateDisk
//
// Creates an instance of a Physical Disk resource and returns a 
// handle to it.
//
// Note:
//   * Do not change the Signature private property of the resource 
//     after it has been created.
//   * To remove the disk from the cluster's control, call 
//     DeleteClusterResource on the returned handle.
// 
// Arguments:
//   IN HCLUSTER hCluster       Cluster handle.
//   IN HGROUP   hGroup         Handle to the group that will contain 
//                              the new resource.
//   IN LPWSTR   lpszDriveLtr   Drive letter of the disk 
//                              for which to create a resource.
//
// Return Value:
//     Resource handle or NULL for non-success. Call GetLastError() 
//     for more info.
//--------------------------------------------------------------------
HRESOURCE ClusDocEx_ResCreateDisk
(
  IN HCLUSTER hCluster,
  IN HGROUP   hGroup,
  IN LPWSTR   lpszDriveLtr
)
{
  HRESOURCE hResource = NULL;

  DWORD dwResult        = ERROR_SUCCESS;
  DWORD dwTestSignature = 0;
  DWORD dwSignature     = 0;
  DWORD dwSyntax        = 0;
  DWORD cbLength        = 0;
  DWORD cbRequired      = 0;
  DWORD cbPosition      = 0;

  LPWSTR lpszResName = ( LPWSTR )LocalAlloc( LPTR, MAX_PATH );
  LPWSTR lpszDrives  = L"Drives ";
  LPVOID pValueList  = NULL;

  BOOL bDiskFound = FALSE;

  CLUSPROP_BUFFER_HELPER cbh;


// Begin property list used to set the Signature private property.
// This example uses a struct to define the property list.

  WCHAR szPropName[] = L"Signature"; 

  typedef struct _DiskSignatureControl 
   {
    DWORD dwPropCount;
    CLUSPROP_PROPERTY_NAME_DECLARE(PropName,sizeof(szPropName)/sizeof(WCHAR));
    CLUSPROP_DISK_SIGNATURE Signature;
    CLUSPROP_SYNTAX Endmark;
   } DiskSignatureControl;

  DiskSignatureControl DSC;

  //  Property Count
  DSC.dwPropCount = 1;

  //  Property Name
  DSC.PropName.Syntax.dw  = CLUSPROP_SYNTAX_NAME;
  DSC.PropName.cbLength   = sizeof( szPropName );
  StringCbCopy( DSC.PropName.sz, DSC.PropName.cbLength, szPropName );

  //  Property Value
  DSC.Signature.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
  DSC.Signature.cbLength  = sizeof( DWORD );
  DSC.Signature.dw        = 0; // this will be changed later
        
  //  Endmark
  DSC.Endmark.dw = CLUSPROP_SYNTAX_ENDMARK;

  DWORD cbSize = sizeof( DiskSignatureControl );

  //  End property list creation

  if( lpszResName == NULL || 
       pValueList == NULL || 
       lpszDrives == NULL )
   {
    goto endf;
   }
    

// Get all available disks
// ClusDocEx_RtpGetControlCodeOutput is defined in 
// "Getting Information with Control Codes."

  pValueList = ClusDocEx_RtpGetControlCodeOutput(
                           L"Physical Disk",
                           hCluster,
                           NULL,
                           CLUSCTL_RESOURCE_TYPE_STORAGE_GET_AVAILABLE_DISKS,
                           &amp;cbRequired );

  if( pValueList == NULL )
   {
    goto endf;
   }



// Parse the value list.
// The architecture of this list is described under 
// "Value Lists for Storage Class Resources".
//
// Two objectives:
// 1) Find the signature of the disk containing the specified drive letter.
// 2) Obtain a list of all drive letters associated with that disk.
//  
// To accomplish both objectives, lpszDrives collects all the drive letters
// for a given disk.  If the specified drive letter is found, the loop
// continues until a new signature signals the start of a new disk. Otherwise
// lpszDrives is reinitialized for each new disk.

  cbh.pb = ( PBYTE )pValueList;

  while( 1 )
   {
    dwSyntax = cbh.pSyntax->dw;

    //  The disk signature structure marks the beginning of a new disk.

    if( dwSyntax == CLUSPROP_SYNTAX_DISK_SIGNATURE )
     {
        
      //  Save the signature in case it contains the drive letter we're looking for.

      dwTestSignature = cbh.pDwordValue->dw;

      if( bDiskFound )
       {
        //  The previous disk contained the specified drive letter
        //  lpszDrives lists all drive letters for that disk
        break;
       }
      else if( lpszDrives != NULL ) 
       {
        //  Clear the drive letter list for the new disk
        LocalFree( lpszDrives );
        lpszDrives = ( LPWSTR )LocalAlloc( LPTR, MAX_PATH );
        if( lpszDrives == NULL ) goto endf;
        StringCbCopy( lpszDrives, 18, L"Drives: " );
       }

     }

    // Will get one partition info structure per disk partition    

    else if( dwSyntax == CLUSPROP_SYNTAX_PARTITION_INFO )
     {
        
      // Add the drive letter of this partition to lpszDrives

      StringCchCatW( lpszDrives, MAX_PATH, cbh.pPartitionInfoValue->szDeviceName ); 
      StringCchCatW( lpszDrives, MAX_PATH, L" " ); 

      if( lstrcmpi( cbh.pPartitionInfoValue->szDeviceName, lpszDriveLtr ) == 0 )
       {
        //  The current disk contains the partition with the drive letter
        //  we're looking for.  Flag the find and save the signature.
        bDiskFound = TRUE;
        dwSignature = dwTestSignature;
       }
     }

    else if( dwSyntax == CLUSPROP_SYNTAX_ENDMARK )
      break;

    cbLength = cbh.pValue->cbLength;

    // If next advance is within value list buffer, 
    // advance the structure pointer.

    cbPosition += ClusDocEx_ListEntrySize( cbLength );

    if( ( cbPosition + sizeof( DWORD ) ) >= cbRequired ) break;

    cbh.pb += ClusDocEx_ListEntrySize( cbLength );

   }

  if( bDiskFound == FALSE ) goto endf;

// Create the resource.  The resource name is "Disk Drives @: @: @: ... " 
// where @ is the drive letter of a disk partition.

  StringCchCopyW( lpszResName, MAX_PATH, L"Disk " );

  StringCchCatW( lpszResName, MAX_PATH, lpszDrives );

  hResource = CreateClusterResource( hGroup,
                                     lpszResName,
                                     L"Physical Disk",
                                     0 );

  if( hResource == NULL )
   {
    dwResult = GetLastError();
    goto endf;
   }

// Update the property list

  DSC.Signature.dw = dwSignature;

// Store the signature in the resource's Signature private property

  dwResult = ClusterResourceControl( hResource,
                                     NULL,
                                     CLUSCTL_RESOURCE_SET_PRIVATE_PROPERTIES,
                                     ( void* ) &amp;DSC,
                                     cbSize,
                                     NULL,
                                     0,
                                     NULL );


  if( dwResult != ERROR_SUCCESS )
   {
    DeleteClusterResource( hResource );
    CloseClusterResource( hResource );
    hResource = NULL;
   }

    
endf:

  LocalFree( pValueList );
  LocalFree( lpszResName );
  LocalFree( lpszDrives );

  SetLastError( dwResult );

  return hResource;
}
//  end ClusDocEx_ResCreateDisk
//--------------------------------------------------------------------
#endif
```



 

 




