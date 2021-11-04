---
description: Outlines the introduction of indexing prioritization and rowset events for Windows 7.
ms.assetid: 6cdfb7d3-f849-432c-960f-912e5024c583
title: Indexing Prioritization and Rowset Events in Windows 7
ms.topic: article
ms.date: 05/31/2018
---

# Indexing Prioritization and Rowset Events in Windows 7

This topic outlines the introduction of indexing prioritization and rowset events for Windows 7.

This topic is organized as follows:

-   [Indexing Prioritization and Rowset Events](#indexing-prioritization-and-rowset-events)
    -   [IRowsetPriorization Examples](#irowsetpriorization-examples)
    -   [IRowsetPrioritization Events](#indexing-prioritization-and-rowset-events-in-windows-7)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Indexing Prioritization and Rowset Events

In Windows 7?and later, there is a priority stack within which the context of any particular query, the client can request that the scopes used in that query be prioritized above that of normal items.

This prioritization stack has the following characteristics:

-   Items in the stack can have foreground, high, or low priority:
    -   **Foreground**: Backoff logic is skipped and indexing proceeds as fast as the machine allows.
    -   **High**: Prioritization has been requested with backoff.
    -   **Low**: Prioritization has been requested, not at the expense of other scopes on the stack, but above non-prioritized indexing.
-   Any request for high or foreground priority bumps the requesting query to the top of the stack automatically.
-   Only the item on top of the stack can have foreground priority.
-   A query with foreground priority that is bumped down in priority receives an event notifying it that it has lost foreground priority and has become a high priority with backoff.

The priority stack sets an overall priority of items that are processed in the indexer as follows:

-   High Priority notifications have no backoff, and are typically sent only for a small number of items. For example, Windows Explorer uses this priority for small copy engine operations.
-   Priority Stack is top of the stack, has backoff, and is the last requested priority query.
-   Second query in the stack.
-   Third query in the stack.
-   Fourth query in the stack, and so forth.
-   Normal Priority items.
-   Deleted items.
    > [!Note]  
    > Items within each group are prioritized internally through the older per-item semantics.

     

### IRowsetPriorization Examples

The primary API for prioritization work is available through the following interface, which can be called by querying the returned rowset:


```
typedef [v1_enum] enum
{
    PRIORITY_LEVEL_FOREGROUND           = 0,    // process items in the scope first as quickly as possible
    PRIORITY_LEVEL_HIGH                 = 1,    // process items in the scope first at the normal rate
    PRIORITY_LEVEL_LOW                  = 2,    // process items in this scope before those at the normal rate, but after any other prioritization requests
    PRIORITY_LEVEL_DEFAULT              = 3     // process items at the normal indexer rate
} PRIORITY_LEVEL;


[
    object,
    uuid(IRowsetPrioritization_GUID),
    pointer_default(unique)
]
interface IRowsetPrioritization : IUnknown
{
    // Sets or retrieves the current indexer prioritization level for the scope specified by
    // this query.

    HRESULT SetScopePriority( [in] PRIORITY_LEVEL priority, [in] DWORD scopeStatisticsEventFrequency );
    HRESULT GetScopePriority( [out] PRIORITY_LEVEL * priority, [out] DWORD * scopeStatisticsEventFrequency );

    // Gets information describing the scope specified by this query:
    // indexedDocumentCount     -   The total number of documents currently indexed in the scope
    // oustandingAddCount       -   The total number of documents yet to be indexed in the scope (those not yet included in indexedDocumentCount)
    // oustandingModifyCount    -   The total number of documents indexed in the scope that need to be re-indexed (included in indexedDocumentCount)
    
    HRESULT GetScopeStatistics( [out] DWORD * indexedDocumentCount, [out] DWORD * oustandingAddCount, [out] DWORD * oustandingModifyCount );
};
```



Rowset prioritization works as follows:

1.  [**IRowsetPrioritization**](/windows/desktop/api/Searchapi/nn-searchapi-irowsetprioritization) is acquired with [IUnknown::QueryInterface Method](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on an indexer rowset. **DBPROP\_ENABLEROWSETEVENTS** must be set to **TRUE** with the OLE DB [ICommandProperties::SetProperties](/previous-versions/windows/desktop/ms711497(v=vs.85)) method prior to executing the query in order to use rowset prioritization.
2.  [**IRowsetPrioritization::SetScopePriority**](/windows/desktop/api/Searchapi/nf-searchapi-irowsetprioritization-setscopepriority) sets the prioritization for the scopes belonging to the query, and the interval the scope statistics event is raised when there are outstanding documents to be indexed within the query scopes. This event is raised if the priority level is set to default.
3.  [**IRowsetPrioritization::GetScopeStatistics**](/windows/desktop/api/Searchapi/nf-searchapi-irowsetprioritization-getscopestatistics) can be used to get the number of indexed items in the scope, the number of outstanding documents to be added in the scope, and the number of documents that need to be re-indexed within this scope.

### IRowsetPrioritization Events

There are three rowset events in [**IRowsetEvents::OnRowsetEvent**](/windows/desktop/api/Searchapi/nf-searchapi-irowsetevents-onrowsetevent) in the [**ROWSETEVENT\_TYPE**](/windows/win32/api/searchapi/ne-searchapi-rowsetevent_type) enumeration:


```
    // This method allows for future notifications of various actions about your rowset or items within
    // eventType:                               - An identifier of the particular event being sent
    // pVarEventData:                           - The expected value of the EventData for each event type
    //      ROWSETEVENT_TYPE_DATAEXPIRED        - VT_EMPTY
    //      ROWSETEVENT_TYPE_FOREGROUNDLOST     - VT_EMPTY
    //      ROWSETEVENT_TYPE_SCOPESTATISTICS    - VT_VECTOR | VT_UI4 - 3 elements (0 = indexed items, 1 = outstanding adds, 2 = oustanding modifies)

    HRESULT OnRowsetEvent( [in] ROWSETEVENT_TYPE eventType, [in] REFPROPVARIANT eventData );
```



The rowset events are as follows:

-   The **ROWSETEVENT\_TYPE\_DATAEXPIRED** event indicates that data backing the rowset has expired, and that a new rowset should be requested.
-   The **ROWSET\_TYPE\_FOREGROUNDLOST** event indicates that an item that did have foreground priority in the prioritization stack has been demoted, because someone else prioritized themselves ahead of this query.
-   The **ROWSETEVENT\_TYPE\_SCOPESTATISTICS** event gives you the same information available from the [**IRowsetPrioritization::GetScopeStatistics**](/windows/desktop/api/Searchapi/nf-searchapi-irowsetprioritization-getscopestatistics) method call, but through a push mechanic, as follows:
    -   The event arises if the prioritization API has been used to request a non-default prioritization level, and a non-zero statistics event frequency.
    -   The event arises only when statistics actually change, and the interval specified in the [**IRowsetPrioritization**](/windows/desktop/api/Searchapi/nn-searchapi-irowsetprioritization) has elapsed (the interval does not guarantee the frequency of the event).
    -   This event is guaranteed to raise a "bounce zero" state (zero items remaining to be added, zero modifies remaining), provided that a non-zero event has been raised.
    -   The indexer may process items without sending this event, if the queue empties before the statistics event frequency.

## Additional Resources

See the following resources related to prioritization and rowsets:

-   Interfaces:
    -   [**IRowsetEvents**](/windows/desktop/api/Searchapi/nn-searchapi-irowsetevents)
    -   [**IRowsetPrioritization**](/windows/desktop/api/Searchapi/nn-searchapi-irowsetprioritization)
-   Enumerations:
    -   [**PRIORITIZE\_FLAGS**](/windows/win32/api/searchapi/ne-searchapi-tagprioritize_flags)
    -   [**PRIORITY\_LEVEL**](/windows/win32/api/searchapi/ne-searchapi-priority_level)
    -   [**ROWSETEVENT\_ITEMSTATE**](/windows/win32/api/searchapi/ne-searchapi-rowsetevent_itemstate)
    -   [**ROWSETEVENT\_TYPE**](/windows/win32/api/searchapi/ne-searchapi-rowsetevent_type)

## Related topics

<dl> <dt>

[Windows 7 Search](./-search-3x-wds-overview.md)
</dt> <dt>

[New for Windows 7 Search](new-for-windows-7-search.md)
</dt> <dt>

[Windows Shell Libraries in Windows 7](-search-win7-development-scenarios.md)
</dt> </dl>

 

 