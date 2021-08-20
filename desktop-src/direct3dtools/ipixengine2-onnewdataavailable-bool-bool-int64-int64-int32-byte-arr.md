---
description: Requests to indicate that the graphics log has new data inside of it.
MS-HAID: vspixengine.IPixEngine2\_OnNewDataAvailable\_BOOL\_BOOL\_INT64\_INT64\_INT32\_BYTE\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixEngine2::OnNewDataAvailable method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: B99FC54C-9395-4B14-93D5-B6408D655DC3
api_name: 
 - IPixEngine2.OnNewDataAvailable
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixengine2_onnewdataavailable_bool_bool_int64_int64_int32_byte_arr"></span>IPixEngine2::OnNewDataAvailable method

Requests to indicate that the graphics log has new data inside of it.

## Syntax


```C++
HRESULT OnNewDataAvailable(
   BOOL    fSessionEnd,
   BOOL    fUnloadCurFrame,
   INT64   i64FilePositionStart,
   INT64   i64FilePositionEnd,
   INT32   iObjectTableDataSize,
   BYTE [] count4_pObjectTableData
);
```

## Parameters

*fSessionEnd*   
true if the session has ended, otherwise false.

*fUnloadCurFrame*   
Not used.

*i64FilePositionStart*   
The file position, in bytes, at which the new data begins.

*i64FilePositionEnd*   
The file position, in bytes, at which the new data ends.

*iObjectTableDataSize*   
The number of bytes contained in count4\_pObjectTableData.

*count4\_pObjectTableData*   
An buffer containing data for the object table.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixEngine2**](/windows/desktop/direct3dtools/ipixengine2)

 

 
