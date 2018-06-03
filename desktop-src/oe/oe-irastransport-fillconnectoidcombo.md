---
title: IRASTransport FillConnectoidCombo method
description: Populates a combo box with entry names from a remote access phonebook.
ms.assetid: ceffcb58-577e-4729-b3cf-1ef61a71561b
keywords:
- FillConnectoidCombo method Windows Mail (formerly Outlook Express)
- FillConnectoidCombo method Windows Mail (formerly Outlook Express) , IRASTransport interface
- IRASTransport interface Windows Mail (formerly Outlook Express) , FillConnectoidCombo method
topic_type:
- apiref
api_name:
- IRASTransport.FillConnectoidCombo
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IRASTransport::FillConnectoidCombo method

\[**IRASTransport::FillConnectoidCombo** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Populates a combo box with entry names from a remote access phonebook.

## Syntax


```C++
HRESULT FillConnectoidCombo(
  [in]  HWND  hwndComboBox,
  [in]  BOOL  fUpdateOnly,
  [out] DWORD *pdwRASResult
);
```



## Parameters

<dl> <dt>

*hwndComboBox* \[in\]
</dt> <dd>

Type: **HWND**

Specifies an **HWND** that contains the handle to the combo box.

</dd> <dt>

*fUpdateOnly* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies a **BOOL** that indicates whether to populate (**TRUE**) or clear (**FALSE**) the combo box.

</dd> <dt>

*pdwRASResult* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains more error information when this method returns IXP\_E\_RAS\_ERROR. Otherwise, it contains NO\_ERROR.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                       | Description                                                                               |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Indicates success. <br/>                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>      | Indicates that *hwndComboBox* is **NULL** or that *fUpdateOnly* is **FALSE**. <br/> |
| <dl> <dt>**IXP\_E\_RAS\_ERROR**</dt> </dl> | Indicates that an error has occurred. <br/>                                         |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





