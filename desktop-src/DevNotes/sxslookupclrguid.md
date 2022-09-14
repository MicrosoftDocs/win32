---
description: Retrieves the class name and other information associated with a given GUID in a component's manifest.
ms.assetid: af7c6e56-604d-4a1b-8fbf-71a372ba1ae7
title: SxsLookupClrGuid function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SxsLookupClrGuid
api_type: 
- DllExport
api_location: 
- Mscoree.dll
- Sxs.dll
---

# SxsLookupClrGuid function

Retrieves the class name and other information associated with a given GUID in a component's manifest. This function is used only when implementing low-level managed-unmanaged interoperability in the .NET Framework. For more information about managed-unmanaged interoperability, see "Interoperating with Unmanaged Code" in the .NET Framework SDK and also [Isolated Applications and Side-by-side Assemblies](../sbscs/isolated-applications-and-side-by-side-assemblies-portal.md).

## Syntax


```C++
BOOL SxsLookupClrGuid(
  _In_        DWORD   dwFlags,
  _In_        LPGUID  pClsid,
  _In_opt_    HANDLE  hActCtx,
  _Inout_opt_ PVOID   pvOutputBuffer,
  _In_        SIZE_T  cbOutputBuffer,
  _Out_       PSIZE_T pcbOutputBuffer
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

A combination of zero or more of the following flags.



| Value                                                                                                                                                                                                                                                                                             | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SXS_LOOKUP_CLR_GUID_USE_ACTCTX"></span><span id="sxs_lookup_clr_guid_use_actctx"></span><dl> <dt>**SXS\_LOOKUP\_CLR\_GUID\_USE\_ACTCTX**</dt> <dt>0x00000001</dt> </dl>              | If this flag is set, then the *hActCtx* parameter must contain an activation-context handle returned by the [**CreateActCtx**](/windows/win32/api/winbase/nf-winbase-createactctxa) function. If this flag is not set, the *hActCtx* parameter is ignored and **SxsLookupClrGuid** searches the activation context that is currently active (the [**ActivateActCtx**](/windows/win32/api/winbase/nf-winbase-activateactctx) function is used to make an activation context active).<br/> |
| <span id="SXS_LOOKUP_CLR_GUID_FIND_SURROGATE"></span><span id="sxs_lookup_clr_guid_find_surrogate"></span><dl> <dt>**SXS\_LOOKUP\_CLR\_GUID\_FIND\_SURROGATE**</dt> <dt>0x00010000</dt> </dl>  | If this flag is set, **SxsLookupClrGuid** searches for a surrogate.<br/>                                                                                                                                                                                                                                                                                                                                                |
| <span id="SXS_LOOKUP_CLR_GUID_FIND_CLR_CLASS"></span><span id="sxs_lookup_clr_guid_find_clr_class"></span><dl> <dt>**SXS\_LOOKUP\_CLR\_GUID\_FIND\_CLR\_CLASS**</dt> <dt>0x00020000</dt> </dl> | If this flag is set, **SxsLookupClrGuid** searches for a class.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| <span id="SXS_LOOKUP_CLR_GUID_FIND_ANY"></span><span id="sxs_lookup_clr_guid_find_any"></span><dl> <dt>**SXS\_LOOKUP\_CLR\_GUID\_FIND\_ANY**</dt> <dt>0x00030000</dt> </dl>                    | This is a combination of the **SXS\_LOOKUP\_CLR\_GUID\_FIND\_SURROGATE** and **SXS\_LOOKUP\_CLR\_GUID\_FIND\_CLR\_CLASS** flags; if both are set, **SxsLookupClrGuid** searches for a surrogate first, and only if it does not find one, then searches for a class.<br/>                                                                                                                                                |



 

</dd> <dt>

*pClsid* \[in\]
</dt> <dd>

A pointer to the GUID about which to search the activation context for interoperation information. This parameter cannot be **NULL**.

</dd> <dt>

*hActCtx* \[in, optional\]
</dt> <dd>

If the **SXS\_LOOKUP\_CLR\_GUID\_USE\_ACTCTX** flag is set in the *dwFlags* parameter, then *hActCtx* must contain an activation-context handle returned by the [**CreateActCtx**](/windows/win32/api/winbase/nf-winbase-createactctxa) function. Otherwise, *hActCtx* is ignored.

</dd> <dt>

*pvOutputBuffer* \[in, out, optional\]
</dt> <dd>

Pointer to the buffer into which return information is copied. This parameter may be NULL-valued only if the *cbOutputBuffer* parameter is zero-valued. The data placed in this buffer on exit (if any) consists of a **SXS\_GUID\_INFORMATION\_CLR** structure followed by any additional string data required. See the Remarks section below for more information.

</dd> <dt>

*cbOutputBuffer* \[in\]
</dt> <dd>

Size in bytes of the buffer pointed to by the *pvOutputBuffer* parameter.

</dd> <dt>

*pcbOutputBuffer* \[out\]
</dt> <dd>

Pointer to a variable where the size, in bytes, of the return information is placed on exit. If the *cbOutputBuffer* parameter is zero, or if the size of the output buffer is smaller than the size of the return information, then **SxsLookupClrGuid** fails and [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns an error of **ERROR\_INSUFFICIENT\_BUFFER**. In this case, use the value in the variable pointed to by *pcbOutputBuffer* to allocate a large enough buffer, and then call **SxsLookupClrGuid** again to retrieve the desired information.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise. For more error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror)

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

Managed components may declare themselves as supporting managed "interop assemblies" so as to allow an unmanaged Win32 component consumer to reference the declaring assembly. The component consumer can interact with the managed component by calling [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) on a GUID. The interoperation layer routes the object creation request to .NET Framework, creates an instance of the managed object, and returns an interface pointer.

**SxsLookupClrGuid** allows the frameworks to retrieve information associated with a given GUID in the component's manifest, such as what its .NET class name is, what version of the .NET Framework it requires, and what host assembly it is located in. Managed components publish an interop assembly that contains a number of statements associating GUIDs with assembly and type names, and the .NET runtime brokers the construction of managed object instances when [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) is called.

The following is a sample component manifest declaring a CLR GUID and a CLR surrogate that **SxsLookupClrGuid** can look up:

``` syntax
<assembly manifestVersion="1.0" xmlns=
    "urn:schemas-microsoft-com:asm.v1">
   <assemblyIdentity type="interop" name=
    "DotNet.Sample.Surrogates" version="1.0.0.0"/>
   <clrClass name="MySampleClass" clsid=
    "{19f7f420-4cc5-4b0d-8a82-c24645c0ba1f}"
      progId="MySampleClass.1" runtimeVersion="1.0.3055"/>
   <clrSurrogate name="MySampleSurrogate" clsid=
    "{fdb46ca5-9477-4528-b4b2-7f00a254cdea}"
      runtimeVersion="1.0.3055"/>
</assembly>
```

An interoperation provider would call **SxsLookupClrGuid** with a pointer to the GUID "{fdb46ca5-9477-4528-b4b2-7f00a254cdea}", and would receive in return the class name "MySampleSurrogate", the required runtime version "1.0.3055", and the textual identity "DotNet.Sample.Surrogates,version='1.0.0.0',type='interop'" of the hosting component.

This return information would be contained and/or referenced by a **SXS\_GUID\_INFORMATION\_CLR** structure declared as follows.

``` syntax
typedef struct _SXS_GUID_INFORMATION_CLR
{
  DWORD   cbSize;
  DWORD   dwFlags;
  PCWSTR  pcwszRuntimeVersion;
  PCWSTR  pcwszTypeName;
  PCWSTR  pcwszAssemblyIdentity;
} SXS_GUID_INFORMATION_CLR, *PSXS_GUID_INFORMATION_CLR;
typedef const SXS_GUID_INFORMATION_CLR *PCSXS_GUID_INFORMATION_CLR;
```

The members of this structure contain the following information.




| Member | Description | 
|--------|-------------|
| <span id="cbSize"></span><span id="cbsize"></span><span id="CBSIZE"></span><strong>cbSize</strong><br /> | Contains the size of the SXS_GUID_INFORMATION_CLR structure (this allows the structure to grow in later versions).<br /> | 
| <span id="dwFlags"></span><span id="dwflags"></span><span id="DWFLAGS"></span><strong>dwFlags</strong><br /> | Contains one of the following two flag values: <br /><ul><li>SXS_GUID_INFORMATION_CLR_FLAG_IS_SURROGATE (0x00000001): Indicates that the specified GUID was associated with a "surrogate."</li><li>SXS_GUID_INFORMATION_CLR_FLAG_IS_CLASS (0x00000002): Indicates that the specified GUID was associated with a "class."</li></ul> | 
| <span id="pcwszRuntimeVersion"></span><span id="pcwszruntimeversion"></span><span id="PCWSZRUNTIMEVERSION"></span><strong>pcwszRuntimeVersion</strong><br /> | Points to a zero-terminated wide-character string that identifies the version of the runtime specified in the host manifest for this class.<br /> | 
| <span id="pcwszTypeName"></span><span id="pcwsztypename"></span><span id="PCWSZTYPENAME"></span><strong>pcwszTypeName</strong><br /> | Points to a zero-terminated wide-character string that contains the name of the .NET class associated with the specified GUID.<br /> | 
| <span id="pcwszAssemblyIdentity"></span><span id="pcwszassemblyidentity"></span><span id="PCWSZASSEMBLYIDENTITY"></span><strong>pcwszAssemblyIdentity</strong><br /> | Points to a zero-terminated wide-character string that contains the textual identity of the assembly that hosts this class. For more information about textual identity, see "Specifying Fully Qualified Type Names" under "Discovering Type Information at Run Time" under "Programming with the .NET Framework" in the .NET Framework SDK.<br /> | 




 

An unmanaged application can use the information returned in this fashion to load the right version of the .NET Framework, load the assembly identified by the **pcwszAssemblyIdentity** element, and then create an instance of the class named by the **pcwszTypeName** element.

## Examples

Use dynamic linking as follows to call the **SxsLookupClrGuid** function:


```C++
#include <windows.h>

// Declare a type for a SxsLookupClrGuid function pointer:
typedef BOOL (WINAPI* PFN_SXS_LOOKUP_CLR_GUID)
    ( IN DWORD      dwFlags,
    IN LPGUID     pClsid,
    IN HANDLE     hActCtx,
    IN OUT PVOID  pvOutputBuffer,
    IN SIZE_T     cbOutputBuffer,
    OUT PSIZE_T   pcbOutputBuffer );

// Declare an actual function pointer
PFN_SXS_LOOKUP_CLR_GUID pfn_SxsLookupClrGuid;

// Declare a handle for the system DLL
HINSTANCE hSxsDll;

// Other declarations:
BOOL isOK;
GUID exampleGuid = 
{0xFDB46CA5, 0x9477, 0x4528, 0xB4, 0xB2, 
    0x7F, 0x00, 0xA2, 0x54, 0xCD, 0xEA};
#define  OUTPUT_BUFFER_SIZE  512
unsigned char outputBuffer[OUTPUT_BUFFER_SIZE];
SIZE_T neededBufferSize;
DWORD errorCode;

#define SXS_LOOKUP_CLR_GUID_USE_ACTCTX       (0x00000001)
#define SXS_LOOKUP_CLR_GUID_FIND_SURROGATE   (0x00010000)
#define SXS_LOOKUP_CLR_GUID_FIND_CLR_CLASS   (0x00020000)
#define SXS_LOOKUP_CLR_GUID_FIND_ANY         (0x00030000) 
    // (SXS_LOOKUP_CLR_GUID_FIND_CLR_CLASS | 
    //    SXS_LOOKUP_CLR_GUID_FIND_SURROGATE)

#define SXS_GUID_INFORMATION_CLR_FLAG_IS_SURROGATE  (0x00000001)
#define SXS_GUID_INFORMATION_CLR_FLAG_IS_CLASS      (0x00000002)

typedef struct _SXS_GUID_INFORMATION_CLR
{
    DWORD       cbSize;
    DWORD       dwFlags;
    PCWSTR      pcwszRuntimeVersion;
    PCWSTR      pcwszTypeName;
    PCWSTR      pcwszAssemblyIdentity;
} SXS_GUID_INFORMATION_CLR, *PSXS_GUID_INFORMATION_CLR;
typedef const SXS_GUID_INFORMATION_CLR *PCSXS_GUID_INFORMATION_CLR;

void main()
{
// Use LoadLibrary to obtain a handle to the "SXS.DLL" system library
  hSxsDll = LoadLibrary( "sxs" );

// If SXS.DLL has loaded properly, 
// try to obtain a pointer to SxsLookupClrGuid
  if( hSxsDll != NULL )
  {
    pfn_SxsLookupClrGuid = (PFN_SXS_LOOKUP_CLR_GUID) GetProcAddress(
                            hSxsDll, "SxsLookupClrGuid" );
    if( pfn_SxsLookupClrGuid == NULL )
    {
       // (Handle failure to find SxsLookupClrGuid here...)
    }
    else
    {
      isOK = (pfn_SxsLookupClrGuid)(
                 SXS_LOOKUP_CLR_GUID_FIND_ANY,     // dwFlags
                 &exampleGuid,                     // pClsid
                 NULL,                             // hActCtx
                 (PVOID) outputBuffer,             // pvOutputBuffer
                 (SIZE_T) OUTPUT_BUFFER_SIZE,      // cbOutputBuffer
                 &neededBufferSize );              // pcbOutputBuffer
      if( isOK == FALSE )
      {
        errorCode = GetLastError( );
        if( errorCode == ERROR_INSUFFICIENT_BUFFER )
        {
          // If the allocation fails because the buffer was too small,
          // allocate a larger output buffer, of the size 
          // now indicated by "neededBufferSize", and try again.
        }
        else
        {
          // Handle other errors here
        }
      }
      else
      {
        // (Use the information here...)
      }
    }
    // Free the library instance when you're done
    FreeLibrary( hSxsDll );
  }
}
```



## Requirements



| Requirement | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Mscoree.dll; </dt> <dt>Sxs.dll</dt> </dl> |



## See also

<dl> <dt>

[Isolated Applications and Side-by-side Assemblies](../sbscs/isolated-applications-and-side-by-side-assemblies-portal.md)
</dt> <dt>

[**CreateActCtx**](/windows/win32/api/winbase/nf-winbase-createactctxa)
</dt> <dt>

[**ActivateActCtx**](/windows/win32/api/winbase/nf-winbase-activateactctx)
</dt> <dt>

[**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance)
</dt> </dl>

 

 
