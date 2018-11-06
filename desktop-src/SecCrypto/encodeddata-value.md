---
Description: Retrieves the encoded data.
ms.assetid: 8e07ac14-6859-410f-ab30-84b8d60a94ad
title: EncodedData.Value property
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- EncodedData.Value
api_type:
- COM
api_location:
- Capicom.dll
---

# EncodedData.Value property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**AsnEncodedData Class**](https://msdn.microsoft.com/library/zt6ys2z1(v=VS.90).aspx) in the [**System.Security.Cryptography**](https://msdn.microsoft.com/library/9eat8fht(v=VS.100).aspx) namespace.\]

The **Value** property retrieves the encoded data. This is the default property.

This property is read-only.

## Syntax


```VB
EncodedData.Value( _
  [ ByVal EncodingType ] _
) As String
```



## Property value

A string that contains the encoded data.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




