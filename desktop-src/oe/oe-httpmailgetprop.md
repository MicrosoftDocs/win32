---
title: HTTPMAILGETPROP structure
description: Contains the response information for the GetProperty and GetPropertyDw methods.
ms.assetid: 96824dc3-01ef-4f02-8a84-0b5eeaf976e8
keywords:
- HTTPMAILGETPROP structure Windows Mail (formerly Outlook Express)
- LPHTTPMAILGETPROP structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPMAILGETPROP
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# HTTPMAILGETPROP structure

\[**HTTPMAILGETPROP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response information for the [**GetProperty**](oe-ihttpmailtransport-getproperty.md) and [**GetPropertyDw**](oe-ihttpmailtransport-getpropertydw.md) methods.

## Syntax


```C++
typedef struct tagHTTPMAILGETPROP {
  HTTPMAILPROPTYPE type;
  LPSTR            pszProp;
  DWORD            dwProp;
} HTTPMAILGETPROP, *LPHTTPMAILGETPROP;
```



## Members

<dl> <dt>

**type**
</dt> <dd>

Type: **[**HTTPMAILPROPTYPE**](oe-httpmailproptype.md)**

</dd> <dd>

Contains a property type from the [**HTTPMAILPROPTYPE**](oe-httpmailproptype.md) enumeration whose value is returned in either **pszProp** or **dwProp**.

</dd> <dt>

**pszProp**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the property value returned by [**GetProperty**](oe-ihttpmailtransport-getproperty.md).

</dd> <dt>

**dwProp**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the property value returned by [**GetPropertyDw**](oe-ihttpmailtransport-getpropertydw.md).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





