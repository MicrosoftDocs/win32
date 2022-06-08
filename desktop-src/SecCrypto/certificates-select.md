---
description: Displays a dialog box for selecting certificates and returns a collection of those certificates selected.
ms.assetid: dbf49a4b-6da1-4819-afcd-46db89a00fce
title: ICertificates2::Select method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificates.Select
- ICertificates2.Select
api_type:
- COM
api_location:
- Capicom.dll
---

# ICertificates2::Select method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2Collection Class**](/previous-versions/windows/embedded/hh424013(v=msdn.10)) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **Select** method displays a dialog box for selecting certificates and returns a collection of those certificates selected. This method was introduced in CAPICOM 2.0.

## Syntax


```VB
Certificates.Select( _
  [ ByVal Title ], _
  [ ByVal DisplayString ], _
  [ ByVal bMultiSelect ] _
)
```



## Parameters

<dl> <dt>

*Title* \[in, optional\]
</dt> <dd>

String that contains the title for the dialog box. The default value is an empty string ("").

</dd> <dt>

*DisplayString* \[in, optional\]
</dt> <dd>

String that contains the prompt text displayed with the dialog box. The default value is an empty string ("").

</dd> <dt>

*bMultiSelect* \[in, optional\]
</dt> <dd>

Boolean value that indicates whether the user can select more than one certificate. True indicates multiple certificates can be selected by using the CTRL or SHIFT key. The default value is false.

</dd> </dl>

## Return value

A [**Certificates**](certificates.md) object that contains the certificates selected from the dialog box.

**CAPICOM 2.1:** The [**Certificates**](certificates.md) object that is returned contains references to the certificates in the collection from which the selection was made. Any changes made to the certificates in the returned **Certificates** object are reflected in that collection.

**CAPICOM 2.0, CAPICOM 2.0.0.1, CAPICOM 2.0.0.2, and CAPICOM 2.0.0.3:** The [**Certificates**](certificates.md) object that is returned contains copies of the certificates in the collection from which the selection was made. Any changes made to the certificates in the returned **Certificates** object are not reflected in that collection.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
