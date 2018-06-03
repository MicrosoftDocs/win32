---
title: Notification Port Example
description: This example show how to display cluster events by creating a notification port in a separate thread.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c3c8ead5-236b-42b3-9413-80df7c71653b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- notification ports Failover Cluster , example
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Notification Port Example

This example show how to display cluster events by creating a notification port in a separate thread.


```C++
//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"  

//////////////////////////////////////////////////////////////////////

//  Constants and global data

    const DWORD MYAPP_EVENTS = ( CLUSTER_CHANGE_GROUP_ADDED      |
                                 CLUSTER_CHANGE_GROUP_DELETED    |
                                 CLUSTER_CHANGE_GROUP_STATE      |
                                 CLUSTER_CHANGE_RESOURCE_ADDED   |
                                 CLUSTER_CHANGE_RESOURCE_DELETED |
                                 CLUSTER_CHANGE_RESOURCE_STATE   |
                                 CLUSTER_CHANGE_HANDLE_CLOSE );


int main()
{
    HCLUSTER  hCluster        = NULL;
    HGROUP    hGroup          = NULL;
    HRESOURCE hRes            = NULL;
    DWORD     dwEventThreadID = 0;
    DWORD     dwExitCode      = 0;  
    HANDLE    hEventThread    = NULL;
    BOOL      bExit           = FALSE;

    hCluster = ClusDocEx_OpenLocalClusterWithName();

    if ( hCluster )
    {
        hEventThread = CreateThread(
                            NULL, 0, ClusDocEx_EventPort, 
                            (LPVOID) hCluster, 0, &amp;dwEventThreadID );

        hGroup = CreateClusterGroup( hCluster, L"EventDemoGroup" );

        if( hGroup )
        {
            hRes = CreateClusterResource( 
                       hGroup, L"EventDemoShare", L"File Share", 0 );
    
            if( hRes )
            {
                OnlineClusterGroup( hGroup, NULL );
                OfflineClusterGroup( hGroup );
                DeleteClusterResource( hRes );
                CloseClusterResource( hRes );
            }

            DeleteClusterGroup( hGroup );               
            CloseClusterGroup( hGroup );
        }

        CloseCluster( hCluster );
    }

    for( ; ; )
    {
        bExit = GetExitCodeThread( hEventThread, &amp;dwExitCode );
        if( bExit &amp;&amp; ( dwExitCode != STILL_ACTIVE ) )
            break;
    }

    if( hEventThread )
        CloseHandle( hEventThread );

    return 0;
}


DWORD WINAPI ClusDocEx_EventPort( LPVOID hCluster )
{
    HCHANGE hChange       = (HCHANGE)INVALID_HANDLE_VALUE ;
    DWORD   dwFilterType;
    DWORD   dwNotifyKey;
    DWORD   dwStatus;
    DWORD   cchNameSize    = ClusDocEx_DEFAULT_CCH;
    LPWSTR  pszObjectName = new WCHAR[cchNameSize];
    bool    bExit = false;
   
    if( hCluster != NULL )
    {
        hChange = CreateClusterNotifyPort( hChange, 
                                           (HCLUSTER) hCluster, 
                                           MYAPP_EVENTS,   //  dwFilter
                                           MYAPP_EVENTS ); //  dwNotifyKey

        while( hChange &amp;&amp; !bExit )
        {
        //  Reset name size 

            cchNameSize = ClusDocEx_DEFAULT_CCH;

            dwStatus = GetClusterNotify( hChange, 
                                         &amp;dwNotifyKey,
                                         &amp;dwFilterType,
                                         pszObjectName,
                                         &amp;cchNameSize,
                                         2500);


            if( dwStatus == ERROR_SUCCESS )
            {
                switch( dwFilterType )
                {
                case CLUSTER_CHANGE_RESOURCE_STATE:
                    wprintf( L"Thread: Receiving resource state change event.\n" );
                    break;

                case CLUSTER_CHANGE_GROUP_STATE:
                    wprintf( L"Thread: Receiving group state change event.\n" );
                    break;

                case CLUSTER_CHANGE_RESOURCE_ADDED: 
                    wprintf( L"Thread: Receiving add resource event.\n" );
                    break;

                case CLUSTER_CHANGE_GROUP_ADDED:
                    wprintf( L"Thread: Receiving add group event.\n" );
                    break;

                case CLUSTER_CHANGE_RESOURCE_DELETED: 
                    wprintf( L"Thread: Receiving delete resource event.\n" );
                    break;

                case CLUSTER_CHANGE_GROUP_DELETED:
                   wprintf( L"Thread: Receiving delete group event.\n" );
                    break;
                case CLUSTER_CHANGE_HANDLE_CLOSE:
                    wprintf( L"Thread: Receiving cluster handle close event.\n" );
                    bExit = true;
                    break;
                }
            }
            else if( dwStatus == WAIT_TIMEOUT )
            {
            //  If any call to GetClusterNotify times out
            //  (exceeds dwMilliseconds, which is 2500 in this case)
            //  any code here will be executed.
            }

        }

        if( hChange ) 
            CloseClusterNotifyPort( hChange );
    }

    LocalFree( pszObjectName );
    return dwStatus;
}
```



 

 




