---
Description: Each of the following sections discusses a function exported by Xenroll.dll. Each section also discusses how to use CertEnroll.dll to replace the function or indicates that no mapping between the two libraries exists.
ms.assetid: 06d8dd6f-7a8d-4da5-a99d-9c9d8fb90cfa
title: Helper Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Helper Functions

Each of the following sections discusses a function exported by Xenroll.dll. Each section also discusses how to use CertEnroll.dll to replace the function or indicates that no mapping between the two libraries exists.

## binaryBlobToString

The [**binaryBlobToString**](https://msdn.microsoft.com/library/windows/desktop/aa385524) function in Xenroll.dll converts a byte array to a string.

Using CertEnroll.dll, you can call the [**VariantByteArrayToString**](/windows/win32/CertEnroll/nf-certenroll-ibinaryconverter-variantbytearraytostring?branch=master) method on the [**IBinaryConverter**](/windows/win32/CertEnroll/nn-certenroll-ibinaryconverter?branch=master) interface.

## stringToBinaryBlob

The [**stringToBinaryBlob**](https://msdn.microsoft.com/library/windows/desktop/aa386145) function in Xenroll.dll converts a string to a byte array.

Using CertEnroll.dll, you can call the [**StringToVariantByteArray**](/windows/win32/CertEnroll/nf-certenroll-ibinaryconverter-stringtovariantbytearray?branch=master) method on the [**IBinaryConverter**](/windows/win32/CertEnroll/nn-certenroll-ibinaryconverter?branch=master) interface.

## Related topics

<dl> <dt>

[Mapping Xenroll.dll to CertEnroll.dll](mapping-xenroll-dll-to-certenroll-dll.md)
</dt> <dt>

[**IBinaryConverter**](/windows/win32/CertEnroll/nn-certenroll-ibinaryconverter?branch=master)
</dt> </dl>

 

 



