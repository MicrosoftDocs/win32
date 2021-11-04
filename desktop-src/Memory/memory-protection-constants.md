---
Description: The following are the memory-protection options; you must specify one of the following values when allocating or protecting a page in memory. Protection attributes cannot be assigned to a portion of a page; they can only be assigned to a whole page.
ms.assetid: 09839db7-2118-4a7d-a707-a08c92bd600c
title: Memory Protection Constants (WinNT.h)
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/27/2020
---

# Memory Protection Constants

The following are the memory-protection options; you must specify one of the following values when allocating or protecting a page in memory. Protection attributes cannot be assigned to a portion of a page; they can only be assigned to a whole page.

## Example

```cpp
STDMETHODIMP CExtBuffer::FInit
    (
    ULONG cItemMax,     //@parm IN | Maximum number of items ever
    ULONG cbItem,       //@parm IN | Size of each item, in bytes
    ULONG cbPage        //@parm IN | Size of system page size (from SysInfo)
    )
{
    BYTE  *pb;

    m_cbReserved = ((cbItem *cItemMax) / cbPage + 1) *cbPage;
    m_rgItem = (BYTE *) VirtualAlloc( NULL, m_cbReserved, MEM_RESERVE, PAGE_READWRITE );

    if (m_rgItem == NULL)
        return ResultFromScode( E_OUTOFMEMORY );

    m_cbItem  = cbItem;
    m_dbAlloc = (cbItem / cbPage + 1) *cbPage;
    pb = (BYTE *) VirtualAlloc( m_rgItem, m_dbAlloc, MEM_COMMIT, PAGE_READWRITE );
    if (pb == NULL)
        {
        VirtualFree((VOID *) m_rgItem, 0, MEM_RELEASE );
        m_rgItem = NULL;
        return ResultFromScode( E_OUTOFMEMORY );
        }

    m_cbAlloc = m_dbAlloc;
    return ResultFromScode( S_OK );
}
```
Example it from [Windows classic samples](https://github.com/microsoft/Windows-classic-samples/blob/1d363ff4bd17d8e20415b92e2ee989d615cc0d91/Samples/Win7Samples/dataaccess/oledb/sampprov/extbuff.cpp) on GitHub.

## Constants


| Constant/value                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PAGE_EXECUTE"></span><span id="page_execute"></span><dl> <dt>**PAGE\_EXECUTE**</dt> <dt>0x10</dt> </dl>                                       | Enables execute access to the committed region of pages. An attempt to write to the committed region results in an access violation.<br/> This flag is not supported by the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="PAGE_EXECUTE_READ"></span><span id="page_execute_read"></span><dl> <dt>**PAGE\_EXECUTE\_READ**</dt> <dt>0x20</dt> </dl>                       | Enables execute or read-only access to the committed region of pages. An attempt to write to the committed region results in an access violation.<br/> **Windows Server 2003 and Windows XP:** This attribute is not supported by the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function until Windows XP with SP2 and Windows Server 2003 with SP1.<br/>                                                                                                                                                                                                                                                                                                                                |
| <span id="PAGE_EXECUTE_READWRITE"></span><span id="page_execute_readwrite"></span><dl> <dt>**PAGE\_EXECUTE\_READWRITE**</dt> <dt>0x40</dt> </dl>        | Enables execute, read-only, or read/write access to the committed region of pages.<br/> **Windows Server 2003 and Windows XP:** This attribute is not supported by the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function until Windows XP with SP2 and Windows Server 2003 with SP1.<br/>                                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="PAGE_EXECUTE_WRITECOPY"></span><span id="page_execute_writecopy"></span><dl> <dt>**PAGE\_EXECUTE\_WRITECOPY**</dt> <dt>0x80</dt> </dl>        | Enables execute, read-only, or copy-on-write access to a mapped view of a file mapping object. An attempt to write to a committed copy-on-write page results in a private copy of the page being made for the process. The private page is marked as **PAGE\_EXECUTE\_READWRITE**, and the change is written to the new page.<br/> This flag is not supported by the [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) or [**VirtualAllocEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex) functions. **Windows Vista, Windows Server 2003 and Windows XP:** This attribute is not supported by the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function until Windows Vista with SP1 and Windows Server 2008.<br/> <br/> |
| <span id="PAGE_NOACCESS"></span><span id="page_noaccess"></span><dl> <dt>**PAGE\_NOACCESS**</dt> <dt>0x01</dt> </dl>                                    | Disables all access to the committed region of pages. An attempt to read from, write to, or execute the committed region results in an access violation.<br/> This flag is not supported by the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="PAGE_READONLY"></span><span id="page_readonly"></span><dl> <dt>**PAGE\_READONLY**</dt> <dt>0x02</dt> </dl>                                    | Enables read-only access to the committed region of pages. An attempt to write to the committed region results in an access violation. If [Data Execution Prevention](data-execution-prevention.md) is enabled, an attempt to execute code in the committed region results in an access violation.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="PAGE_READWRITE"></span><span id="page_readwrite"></span><dl> <dt>**PAGE\_READWRITE**</dt> <dt>0x04</dt> </dl>                                 | Enables read-only or read/write access to the committed region of pages. If [Data Execution Prevention](data-execution-prevention.md) is enabled, attempting to execute code in the committed region results in an access violation.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <span id="PAGE_WRITECOPY"></span><span id="page_writecopy"></span><dl> <dt>**PAGE\_WRITECOPY**</dt> <dt>0x08</dt> </dl>                                 | Enables read-only or copy-on-write access to a mapped view of a file mapping object. An attempt to write to a committed copy-on-write page results in a private copy of the page being made for the process. The private page is marked as **PAGE\_READWRITE**, and the change is written to the new page. If [Data Execution Prevention](data-execution-prevention.md) is enabled, attempting to execute code in the committed region results in an access violation.<br/> This flag is not supported by the [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) or [**VirtualAllocEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex) functions.<br/>                                                                               |
| <span id="PAGE_TARGETS_INVALID"></span><span id="page_targets_invalid"></span><dl> <dt>**PAGE\_TARGETS\_INVALID**</dt> <dt>0x40000000</dt> </dl>        | Sets all locations in the pages as invalid targets for CFG. Used along with any execute page protection like **PAGE\_EXECUTE**, **PAGE\_EXECUTE\_READ**, **PAGE\_EXECUTE\_READWRITE** and **PAGE\_EXECUTE\_WRITECOPY**. Any indirect call to locations in those pages will fail CFG checks and the process will be terminated. The default behavior for executable pages allocated is to be marked valid call targets for CFG.<br/> This flag is not supported by the [**VirtualProtect**](/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect) or [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) functions.<br/>                                                                                                              |
| <span id="PAGE_TARGETS_NO_UPDATE"></span><span id="page_targets_no_update"></span><dl> <dt>**PAGE\_TARGETS\_NO\_UPDATE**</dt> <dt>0x40000000</dt> </dl> | Pages in the region will not have their CFG information updated while the protection changes for [**VirtualProtect**](/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect). For example, if the pages in the region was allocated using **PAGE\_TARGETS\_INVALID**, then the invalid information will be maintained while the page protection changes. This flag is only valid when the protection changes to an executable type like **PAGE\_EXECUTE**, **PAGE\_EXECUTE\_READ**, **PAGE\_EXECUTE\_READWRITE** and **PAGE\_EXECUTE\_WRITECOPY**. The default behavior for **VirtualProtect** protection change to executable is to mark all locations as valid call targets for CFG. <br/>                                           |



The following are modifiers that can be used in addition to the options provided in the previous table, except as noted.



| Constant/value                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PAGE_GUARD"></span><span id="page_guard"></span><dl> <dt>**PAGE\_GUARD**</dt> <dt>0x100</dt> </dl>                      | Pages in the region become guard pages. Any attempt to access a guard page causes the system to raise a **STATUS\_GUARD\_PAGE\_VIOLATION** exception and turn off the guard page status. Guard pages thus act as a one-time access alarm. For more information, see [Creating Guard Pages](creating-guard-pages.md).<br/> When an access attempt leads the system to turn off guard page status, the underlying page protection takes over.<br/> If a guard page exception occurs during a system service, the service typically returns a failure status indicator.<br/> This value cannot be used with **PAGE\_NOACCESS**.<br/> This flag is not supported by the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function.<br/>                                                                                                                                                                                                                              |
| <span id="PAGE_NOCACHE"></span><span id="page_nocache"></span><dl> <dt>**PAGE\_NOCACHE**</dt> <dt>0x200</dt> </dl>                | Sets all pages to be non-cachable. Applications should not use this attribute except when explicitly required for a device. Using the interlocked functions with memory that is mapped with **SEC\_NOCACHE** can result in an **EXCEPTION\_ILLEGAL\_INSTRUCTION** exception.<br/> The **PAGE\_NOCACHE** flag cannot be used with the **PAGE\_GUARD**, **PAGE\_NOACCESS**, or **PAGE\_WRITECOMBINE** flags.<br/> The **PAGE\_NOCACHE** flag can be used only when allocating private memory with the [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc), [**VirtualAllocEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex), or [**VirtualAllocExNuma**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocexnuma) functions. To enable non-cached memory access for shared memory, specify the **SEC\_NOCACHE** flag when calling the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function.<br/>                                                                                                                                                   |
| <span id="PAGE_WRITECOMBINE"></span><span id="page_writecombine"></span><dl> <dt>**PAGE\_WRITECOMBINE**</dt> <dt>0x400</dt> </dl> | Sets all pages to be write-combined. <br/> Applications should not use this attribute except when explicitly required for a device. Using the interlocked functions with memory that is mapped as write-combined can result in an **EXCEPTION\_ILLEGAL\_INSTRUCTION** exception. <br/> The **PAGE\_WRITECOMBINE** flag cannot be specified with the **PAGE\_NOACCESS**, **PAGE\_GUARD**, and **PAGE\_NOCACHE** flags. <br/> The **PAGE\_WRITECOMBINE** flag can be used only when allocating private memory with the [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc), [**VirtualAllocEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex), or [**VirtualAllocExNuma**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocexnuma) functions. To enable write-combined memory access for shared memory, specify the **SEC\_WRITECOMBINE** flag when calling the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function.<br/> **Windows Server 2003 and Windows XP:** This flag is not supported until Windows Server 2003 with SP1.<br/> |



The following constants can only be used with the [**LoadEnclaveData**](/windows/desktop/api/enclaveapi/nf-enclaveapi-loadenclavedata) function when you specify an enclave that has the Intel Software Guard Extensions (SGX) architecture.



| Constant                                                                                                                                                                                                  | Description                                                                                                                                 |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PAGE_ENCLAVE_THREAD_CONTROL"></span><span id="page_enclave_thread_control"></span><dl> <dt>**PAGE\_ENCLAVE\_THREAD\_CONTROL**</dt> </dl> | The page contains a thread control structure (TCS).<br/>                                                                              |
| <span id="PAGE_ENCLAVE_UNVALIDATED"></span><span id="page_enclave_unvalidated"></span><dl> <dt>**PAGE\_ENCLAVE\_UNVALIDATED**</dt> </dl>           | The page contents that you supply are excluded from measurement with the EEXTEND instruction of the Intel SGX programming model.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>WinNT.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga)
</dt> <dt>

[Memory Protection](memory-protection.md)
</dt> <dt>

[**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc)
</dt> <dt>

[**VirtualAllocEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex)
</dt> <dt>

[**LoadEnclaveData**](/windows/desktop/api/enclaveapi/nf-enclaveapi-loadenclavedata)
</dt> </dl>

 

 
