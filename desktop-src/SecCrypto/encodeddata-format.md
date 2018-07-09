---
Description: Returns a string representation of the encoded data.
ms.assetid: d1231e6d-57d7-4b5a-ab37-d4ee1b29cf25
title: EncodedData.Format method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EncodedData.Format
api_type: 
- COM
api_location: 
- Capicom.dll
---

# EncodedData.Format method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**AsnEncodedData Class**](https://www.bing.com/search?q=**AsnEncodedData+Class**) in the [**System.Security.Cryptography**](https://www.bing.com/search?q=**System.Security.Cryptography**) namespace.\]

The **Format** method returns a string representation of the encoded data.

## Syntax


```VB
EncodedData.Format( _
  [ ByVal bMultiLines ] _
)
```



## Parameters

<dl> <dt>

*bMultiLines* \[in, optional\]
</dt> <dd>

Boolean value that indicates whether the returned string contains multiple lines. If **True**, the returned string may contain multiple lines separated by **vbCrLf**. The default value is **False**.

</dd> </dl>

## Return value

A human-readable string that represents the encoded data. If CAPICOM does not understand the encoded data, a hexadecimal representation of the data is returned.

## Remarks

The format of the returned string may change between different versions of CAPICOM. Do not rely on any particular format in your application.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**EncodedData**](encodeddata.md)
</dt> </dl>

 

 




