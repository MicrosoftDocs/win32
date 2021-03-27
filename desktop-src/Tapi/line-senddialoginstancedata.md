---
description: The TSPI LINE\_SENDDIALOGINSTANCEDATA message causes TAPI to call the TUISPI\_providerGenericDialogData function in the UI DLL associated with htDlgInst, passing it the parameter block pointed to by lpParams, of length dwSize.
ms.assetid: d3c176ba-8b4b-4b7c-a603-130dfa761898
title: LINE_SENDDIALOGINSTANCEDATA message (Tspi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_SENDDIALOGINSTANCEDATA message

The TSPI **LINE\_SENDDIALOGINSTANCEDATA** message causes TAPI to call the [**TUISPI\_providerGenericDialogData**](/windows/win32/api/tspi/nf-tspi-tuispi_providergenericdialogdata) function in the UI DLL associated with *htDlgInst*, passing it the parameter block pointed to by *lpParams*, of length *dwSize*.


```C++
            
```



## Parameters

<dl> <dt>

*htDlgInst* 
</dt> <dd>

The HTAPIDIALOGINSTANCE that was returned to the service provider when the dialog box instance was created using [**LINE\_CREATEDIALOGINSTANCE**](line-createdialoginstance.md).

</dd> <dt>

*lpParams* 
</dt> <dd>

Pointer to a provider-specific parameter block that is conveyed to the UI DLL [**TUISPI\_providerGenericDialogData**](/windows/win32/api/tspi/nf-tspi-tuispi_providergenericdialogdata) function, the size of which is specified by *dwSize*. If this parameter is set to **NULL**, this is a request to close the dialog box immediately and clean up (the UI DLL should not invoke [**TUISPIDLLCALLBACK**](/windows/win32/api/tspi/nc-tspi-tuispidllcallback) during this cleanup).

</dd> <dt>

*dwSize* 
</dt> <dd>

The size in bytes of the parameter block to be conveyed to the UI DLL.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tspi.h</dt> </dl> |



## See also

<dl> <dt>

[**TUISPIDLLCALLBACK**](/windows/win32/api/tspi/nc-tspi-tuispidllcallback)
</dt> <dt>

[**TUISPI\_providerGenericDialogData**](/windows/win32/api/tspi/nf-tspi-tuispi_providergenericdialogdata)
</dt> <dt>

[**LINE\_CREATEDIALOGINSTANCE**](line-createdialoginstance.md)
</dt> </dl>

 

