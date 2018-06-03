---
title: Using Column Persistence Implementation Details
description: This section includes information about how to add snap-in support for the CCF\_COLUMN\_SET\_ID clipboard format and how to access column configuration data using the IColumnData interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 26d208a3-ce36-4baf-91b7-2579dfcc7c6a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- column persistence MMC , implementation details
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Column Persistence: Implementation Details

This section includes information about how to add snap-in support for the [**CCF\_COLUMN\_SET\_ID**](ccf-column-set-id.md) clipboard format and how to access column configuration data using the [**IColumnData**](/windows/desktop/api/Mmc/nn-mmc-icolumndata) interface.

**To add snap-in support for CCF\_COLUMN\_SET\_ID**

1.  Add the CCF\_COLUMN\_SET\_ID clipboard format to the snap-in's [**IDataObject**](https://www.bing.com/search?q=**IDataObject**) implementation. Usually, **IDataObject** has its supported clipboard formats as static members. If so, add the CCF\_COLUMN\_SET\_ID format as a member.
    ```C++
    static UINT s_cfColumnSetID;
    ```

    

2.  Register the CCF\_COLUMN\_SET\_ID format and assign the registered format to the static member in the [**IDataObject**](https://www.bing.com/search?q=**IDataObject**) implementation's constructor.
    ```C++
    s_cfColumnSetID = RegisterClipboardFormat (W2T(CCF_COLUMN_SET_ID));
    ```

    

3.  Include support for the CCF\_COLUMN\_SET\_ID format in the snap-in's implementation of the [**IDataObject::GetData**](https://www.bing.com/search?q=**IDataObject::GetData**) method.

Before using the [**IColumnData**](/windows/desktop/api/Mmc/nn-mmc-icolumndata) interface, review the topics [Using IColumnData](using-icolumndata.md) and [IHeaderCtrl2 and Column Persistence](iheaderctrl2-and-column-persistence.md).

**To access column configuration data using IColumnData**

1.  The [**IColumnData**](/windows/desktop/api/Mmc/nn-mmc-icolumndata) interface can be queried from the [**IConsole2**](/windows/desktop/api/Mmc/nn-mmc-iconsole2) passed into [**IComponent::Initialize**](/windows/desktop/api/Mmc/nf-mmc-icomponent-initialize) during the component's creation.
2.  To retrieve and set the current width, order, and hidden status of columns in a column set, use the [**GetColumnConfigData**](/windows/desktop/api/Mmc/nf-mmc-icolumndata-getcolumnconfigdata) and [**SetColumnConfigData**](/windows/desktop/api/Mmc/nf-mmc-icolumndata-setcolumnconfigdata) methods. To retrieve and set the sorted column and sorting direction for columns in a column set, use the [**GetColumnSortData**](/windows/desktop/api/Mmc/nf-mmc-icolumndata-getcolumnsortdata) and [**SetColumnSortData**](/windows/desktop/api/Mmc/nf-mmc-icolumndata-setcolumnsortdata) methods.
3.  When calling any of the [**IColumnData**](/windows/desktop/api/Mmc/nn-mmc-icolumndata) methods, fill an [**SColumnSetID**](/windows/desktop/api/Mmc/ns-mmc-_scolumnsetid) structure to specify the ID of the column set on which the particular action is performed. If the snap-in does not support the CCF\_COLUMN\_SET\_ID clipboard format, the column set ID is the node type GUID of the scope item that owns the list view. If the clipboard format is supported, the ID of the column set is the same one supplied to MMC in the snap-in's [**IDataObject::GetData**](https://www.bing.com/search?q=**IDataObject::GetData**) implementation.

## Related topics

<dl> <dt>

[Using Column Persistence](using-column-persistence.md)
</dt> <dt>

[Using Column Persistence: Interfaces](using-column-persistence-interfaces.md)
</dt> <dt>

[Using Column Persistence: Advanced Topics](using-column-persistence-advanced-topics.md)
</dt> </dl>

 

 




