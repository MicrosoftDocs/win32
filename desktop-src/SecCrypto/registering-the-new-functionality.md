---
Description: Support for registering the new functionality in a system registry must be provided in the new DLL along with the new function.
ms.assetid: 7a6af325-4891-40db-8d33-c9782bd438e5
title: Registering the New Functionality
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registering the New Functionality

Support for registering the new functionality in a system registry must be provided in the new DLL along with the new function. [OID Support Functions](https://www.bing.com/search?q=OID Support Functions) provide assistance with this registration. Regsvr32.exe registers new functions. This tool is included with Windows.

The new DLL must provide [**DllRegisterServer**](https://www.bing.com/search?q=**DllRegisterServer**) and [**DllUnregisterServer**](https://www.bing.com/search?q=**DllUnregisterServer**) entry points for use by Regsvr32.exe. [*CryptoAPI*](https://www.bing.com/search?q=*CryptoAPI*) functions, such as [**CryptRegisterOIDFunction**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptregisteroidfunction) or [**CryptUnregisterOIDFunction**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptunregisteroidfunction), can be used within these entry points, as shown in the following example.


```C++
//  The DllRegisterServer Entry Point
STDAPI DllRegisterServer(void)
{
    if(!CryptRegisterOIDFunction(
         X509_ASN_ENCODING,                  // Encoding type
         CRYPT_OID_ENCODE_OBJECT_FUNC,       // Function name
         szOID_NEW_CERTIFICATE_TYPE,         // OID
         L"NewCert.dll",                     // Dll name
         L"NewCertificateTypeEncodeObject"   // Override function
         ))                                  //   name
       {
         return E_FAIL;
       }
    else
       {
         return S_OK;
       }
}

// The DllUnregisterServer Entry Point
STDAPI DllUnregisterServer(void)
{
    HRESULT     hr = S_OK;

    if(!CryptUnregisterOIDFunction(
          X509_ASN_ENCODING,             // Encoding type
          CRYPT_OID_ENCODE_OBJECT_FUNC,  // Function name
          szOID_NEW_CERTIFICATE_TYPE     // OID
          ))
    {
       if(ERROR_FILE_NOT_FOUND != GetLastError())
               hr = E_FAIL;
    }
    return hr;
}
```



This example must be compiled and linked into the new DLL. These two entry points, along with the function entry point, must be exported.

To install the new functionality on a computer, run Regsvr32.exe from a command prompt, specifying the name and path of the new DLL. Regsvr32.exe accesses the [**CryptRegisterOIDFunction**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptregisteroidfunction) function through the [**DllRegisterServer**](https://msdn.microsoft.com/windows/desktop/f5db85f8-41ce-404d-b5de-f8b2eab8f7e0) function entry point and registers the new function and DLL.

 

 



