---
Description: 'The GetGroupCount method retrieves the number of groups that are contained in the timeline.'
ms.assetid: '24351e03-3132-4363-8171-eae517fb770a'
title: 'IAMTimeline::GetGroupCount method'
---

# IAMTimeline::GetGroupCount method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetGroupCount` method retrieves the number of groups that are contained in the timeline.

## Syntax


```C++
HRESULT GetGroupCount(
   long *pCount
);
```



## Parameters

<dl> <dt>

*pCount* 
</dt> <dd>

Receives the number of groups in the timeline.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimeline Interface**](iamtimeline.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




