---
Description: Displaying the Status of a Catalog
ms.assetid: d0a80948-0a23-4af3-8036-0d1471441624
title: Displaying the Status of a Catalog
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Displaying the Status of a Catalog

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following code segment is the **DisplayStatus** function of the sample, which uses the [**CISTATE**](/windows/desktop/api/Ntquery/nf-ntquery-cistate) structure, the [**CI\_STATE\_\***](ci-state-constants.md) constants, and the **CIState** function of the [OLE DB Helper API](https://www.bing.com/search?q=OLE DB Helper API) to determine the status of the specified catalog. It outputs the status using the sample's **DisplayStat** function and the IDS\_\* strings defined in QSample.rc.


```C++
HRESULT DisplayStatus(
    WCHAR const * pwcCatalog,
    WCHAR const * pwcMachine,
    LCID          lcid )
{
    CI_STATE state;
    state.cbStruct = sizeof state;

    DisplayStat( pwcMachine, IDS_STAT_MACHINE );
    DisplayStat( pwcCatalog, IDS_STAT_CATALOG );

    HRESULT hr = CIState( pwcCatalog, pwcMachine, &amp;state );

    if ( SUCCEEDED( hr ) )
    {
        DisplayStat( state.cTotalDocuments, IDS_STAT_TOTALDOCUMENTS );
        DisplayStat( state.cFreshTest, IDS_STAT_FRESHTEST );
        DisplayStat( state.cFilteredDocuments, IDS_STAT_FILTEREDDOCUMENTS );
        DisplayStat( state.cDocuments, IDS_STAT_DOCUMENTS );
        DisplayStat( state.cSecQDocuments, IDS_STAT_SECQDOCUMENTS );
        DisplayStat( state.cUniqueKeys, IDS_STAT_UNIQUEKEYS );
        DisplayStat( state.cWordList, IDS_STAT_WORDLIST );
        DisplayStat( state.cPersistentIndex, IDS_STAT_PERSISTENTINDEX );
        DisplayStat( state.cQueries, IDS_STAT_QUERIES );
        DisplayStat( state.dwIndexSize, IDS_STAT_INDEXSIZE );
        DisplayStat( state.dwPropCacheSize / 1024, IDS_STAT_PROPCACHESIZE );

        DisplayStat( ( state.eState & CI_STATE_SCANNING ) ?
                     state.cPendingScans : 0,
                     IDS_STAT_SCANS );

        const DWORD ALL_CI_MERGE = ( CI_STATE_SHADOW_MERGE |
                                     CI_STATE_ANNEALING_MERGE |
                                     CI_STATE_INDEX_MIGRATION_MERGE |
                                     CI_STATE_MASTER_MERGE |
                                     CI_STATE_MASTER_MERGE_PAUSED );

        if ( 0 != ( ALL_CI_MERGE & state.eState ) )
        {
            UINT idStr;
            if ( state.eState & CI_STATE_SHADOW_MERGE )
                idStr = IDS_STAT_MERGE_SHADOW;
            else if ( state.eState & CI_STATE_ANNEALING_MERGE )
                idStr = IDS_STAT_MERGE_ANNEALING;
            else if ( state.eState & CI_STATE_INDEX_MIGRATION_MERGE )
                idStr = IDS_STAT_MERGE_INDEX_MIGRATION;
            else if ( state.eState & CI_STATE_MASTER_MERGE )
                idStr = IDS_STAT_MERGE_MASTER;
            else
                idStr = IDS_STAT_MERGE_MASTER_PAUSED;

            DisplayStat( state.dwMergeProgress, idStr );
        }

        if ( CI_STATE_READ_ONLY & state.eState )
            DisplayStat( IDS_STAT_READ_ONLY );
        if ( CI_STATE_RECOVERING & state.eState )
            DisplayStat( IDS_STAT_RECOVERING );
        if ( CI_STATE_LOW_MEMORY & state.eState )
            DisplayStat( IDS_STAT_LOW_MEMORY );
        if ( CI_STATE_HIGH_IO & state.eState )
            DisplayStat( IDS_STAT_HIGH_IO );
        if ( CI_STATE_BATTERY_POWER & state.eState )
            DisplayStat( IDS_STAT_BATTERY_POWER );
        if ( CI_STATE_USER_ACTIVE & state.eState )
            DisplayStat( IDS_STAT_USER_ACTIVE );
        if ( CI_STATE_STARTING & state.eState )
            DisplayStat( IDS_STAT_STARTING );
        if ( CI_STATE_READING_USNS & state.eState )
            DisplayStat( IDS_STAT_READING_USNS );
    }
    else
    {
        DisplayError( IDS_CANTDISPLAYSTATUS, pwcCatalog, hr, lcid );
    }

    return hr;
}
```



 

 



