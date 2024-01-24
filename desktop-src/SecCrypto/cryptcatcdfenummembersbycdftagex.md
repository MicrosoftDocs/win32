---
description: Enumerates the individual file members in the CatalogFiles section of a catalog definition file (CDF).
ms.assetid: 38e17ef2-65dc-45f8-a484-8eedcf4ce3e3
title: CryptCATCDFEnumMembersByCDFTagEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CryptCATCDFEnumMembersByCDFTagEx
api_type: 
- DllExport
api_location: 
- Wintrust.dll
---

# CryptCATCDFEnumMembersByCDFTagEx function

\[The **CryptCATCDFEnumMembersByCDFTagEx** function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The **CryptCATCDFEnumMembersByCDFTagEx** function enumerates the individual file members in the **CatalogFiles** section of a catalog definition file (CDF). **CryptCATCDFEnumMembersByCDFTagEx** is called by [MakeCat](makecat.md).

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
LPWSTR WINAPI CryptCATCDFEnumMembersByCDFTagEx(
  _In_    CRYPTCATCDF                  *pCDF,
  _Inout_ LPWSTR                       pwszPrevCDFTag,
  _In_    PFN_CDF_PARSE_ERROR_CALLBACK pfnParseError,
  _In_    CRYPTCATMEMBER               **ppMember,
  _In_    BOOL                         fContinueOnError,
  _In_    LPVOID                       pvReserved
);
```



## Parameters

<dl> <dt>

*pCDF* \[in\]
</dt> <dd>

A pointer to a [**CRYPTCATCDF**](/windows/win32/api/mscat/ns-mscat-cryptcatcdf) structure.

</dd> <dt>

*pwszPrevCDFTag* \[in, out\]
</dt> <dd>

A pointer to a **null**-terminated string that identifies the catalog file member.

</dd> <dt>

*pfnParseError* \[in\]
</dt> <dd>

A pointer to a user-defined function to handle file parse errors.

</dd> <dt>

*ppMember* \[in\]
</dt> <dd>

A pointer to a [**CRYPTCATMEMBER**](/windows/win32/api/mscat/ns-mscat-cryptcatmember) structure that contains the file member information.

</dd> <dt>

*fContinueOnError* \[in\]
</dt> <dd>

A value that specifies whether to keep in memory a reference to the last enumerated member.

</dd> <dt>

*pvReserved* \[in\]
</dt> <dd>

This parameter is reserved; do not use it.

</dd> </dl>

## Return value

Upon success, this function returns a pointer to a **null**-terminated string that identifies a file member in the **CatalogFiles** section of a CDF. The **CryptCATCDFEnumMembersByCDFTagEx** function returns a **NULL** pointer if it fails.

## Remarks

You typically call this function in a loop to enumerate all of the catalog file members in a CDF. Before entering the loop, set *pwszPrevCDFTag* to **NULL**. The function returns a pointer to the first member. Set *pwszPrevCDFTag* to the return value of the function for subsequent iterations of the loop.

## Examples

The following example shows the correct sequence of assignments for the *pwszPrevCDFTag* parameter (`pwszMemberTag`).


```C++
    CRYPTCATMEMBER      *pMember;
    LPWSTR              pwszMemberTag;
    CRYPTCATCDF         *pCDF;

    pCDF = CryptCATCDFOpen(L'myCDF', NULL);
    

    pMember = NULL;
    pwszMemberTag = NULL;

    while (pwszMemberTag = CryptCATCDFEnumMembersByCDFTagEx(pCDF,
                                                            pwszMemberTag,
                                                            NULL,
                                                            &pMember,
                                                            FALSE,
                                                            NULL))
    {
        //do something with pwszMemberTag and pMember
    }

    CryptCATCDFClose(pCDF);
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Wintrust.dll</dt> </dl> |



## See also

<dl> <dt>

[MakeCat](makecat.md)
</dt> <dt>

[**CRYPTCATCDF**](/windows/win32/api/mscat/ns-mscat-cryptcatcdf)
</dt> <dt>

[**CRYPTCATMEMBER**](/windows/win32/api/mscat/ns-mscat-cryptcatmember)
</dt> <dt>

[**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress)
</dt> <dt>

[**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya)
</dt> </dl>

 

 
