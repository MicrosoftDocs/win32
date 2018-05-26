---
title: INNTPTransport CommandNEWGROUPS method
description: Retrieves the list of newsgroups which have been added to the server since the date specified in pstLast.
ms.assetid: c6a27dc0-5433-48ad-ad9b-93b812951c9e
keywords:
- CommandNEWGROUPS method Windows Mail (formerly Outlook Express)
- CommandNEWGROUPS method Windows Mail (formerly Outlook Express) , INNTPTransport interface
- INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandNEWGROUPS method
topic_type:
- apiref
api_name:
- INNTPTransport.CommandNEWGROUPS
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INNTPTransport::CommandNEWGROUPS method

\[**INNTPTransport::CommandNEWGROUPS** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the list of newsgroups which have been added to the server since the date specified in *pstLast*. The caller can restrict the list by specifying a list of distributions in *pszDist*. For example: CommandNEWGROUPS(&stLast, "alt.tv") returns the list of newsgroups that begin with "alt.tv" that have been added to the server since the time in *pstLast*.

## Syntax


```C++
HRESULT CommandNEWGROUPS(
  [in] SYSTEMTIME *pstLast,
  [in] LPSTR      pszDist
);
```



## Parameters

<dl> <dt>

*pstLast* \[in\]
</dt> <dd>

Type: **SYSTEMTIME\***

The time to specify as the last time groups were checked.

</dd> <dt>

*pszDist* \[in\]
</dt> <dd>

Type: **LPSTR**

Distributions to check. This can be a single dist such as "alt" or a list of dists such as "alt.tv,comp". The list of distributions must be separated by commas.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | An invalid parameter was passed in<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | A memory allocation failed<br/>         |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





