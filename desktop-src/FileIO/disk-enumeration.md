---
description: Enumerate disk device interfaces with GUID_DEVINTERFACE_DISK to discover disk device paths across the legacy and Native NVMe storage stacks.
title: Disk Enumeration
ms.topic: how-to
ms.date: 10/26/2026
# customer intent: As a Windows app developer, I want to enumerate disk device interfaces so that my application can discover disk device paths across storage stacks.
---

# Disk enumeration

[GUID_DEVINTERFACE_DISK](/windows-hardware/drivers/install/guid-devinterface-disk) identifies the disk device interface class. The system-supplied disk class drivers register instances of this class for the disks they expose. Enumerating its enabled instances is the stack-agnostic way to discover disk device paths: both the legacy stack and the Native NVMe stack expose this interface class.

This is why you should enumerate the *interface* GUID rather than keying off a setup-class GUID, such as [GUID_DEVCLASS_DISKDRIVE](/windows-hardware/drivers/install/system-defined-device-setup-classes-available-to-vendors), which is not guaranteed to be stack-agnostic.

## Interface GUID vs. device class GUID

[GUID_DEVINTERFACE_DISK](/windows-hardware/drivers/install/guid-devinterface-disk) and [GUID_DEVCLASS_DISKDRIVE](/windows-hardware/drivers/install/system-defined-device-setup-classes-available-to-vendors) answer different questions and are not interchangeable:

- `GUID_DEVINTERFACE_DISK` identifies an interface class, not an individual device path. Enumerating its enabled instances returns symbolic-link paths that applications can pass to [CreateFileW](/windows/win32/api/fileapi/nf-fileapi-createfilew). The resulting handle can be used for operations supported by the target disk, subject to the requested access rights and applicable permissions. An enumerated path is not a guarantee that opening the disk will succeed: the device may be removed or become unavailable before the open request completes.
- `GUID_DEVCLASS_DISKDRIVE` is a device setup class used by PnP/SetupAPI for device installation and classification, such as driver installation, Device Manager grouping, INF matching, and similar servicing tasks. A device instance belonging to this setup class is not guaranteed to expose an interface you can open, and enumerating by setup class says nothing about which functional interfaces, if any, that device instance currently exposes.
- The legacy disk stack (`disk.sys`/`classpnp.sys`) uses the `GUID_DEVCLASS_DISKDRIVE` setup class, while the Native NVMe stack (`nvmedisk.sys`) uses its own, different setup class, [`{75416e63-5912-4dfa-ae8f-3efaccaffb14}`](/windows-hardware/drivers/install/system-defined-device-setup-classes-available-to-vendors). Enumerating only `GUID_DEVCLASS_DISKDRIVE` would therefore miss every disk managed by the Native NVMe stack. `GUID_DEVINTERFACE_DISK` does not have this gap, since both stacks register the same interface for each disk they manage.

## Enumeration scope

This sample performs a one-time enumeration of currently enabled disk device interfaces. It does not enumerate volumes or drive letters, and the returned list is not a continuously maintained inventory.

`CM_GET_DEVICE_INTERFACE_LIST_PRESENT` selects present/enabled interfaces. It does not indicate whether a disk is online in Disk Management.

For a long-running application that tracks arrivals and removals, register device-interface notifications with [CM_Register_Notification](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) before performing the initial enumeration. Reconcile notifications with the initial list and handle duplicates, because an arriving interface can appear in both. Release the notification registration with [CM_Unregister_Notification](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification) when finished. Device removal can still race with opening a path or performing I/O.

## Sample code: enumerate disks

> [!NOTE]
> Retrying handles changes between the size query and list retrieval; it does not guarantee eventual success or continued availability of the returned devices. The sample retries `CR_BUFFER_SMALL` without an attempt limit, so repeated interface arrivals can theoretically keep it retrying indefinitely. Other failures are reported and terminate enumeration.

```c
#define INITGUID
#include <windows.h>
#include <ntddstor.h>     // GUID_DEVINTERFACE_DISK
#include <cfgmgr32.h>
#include <stdio.h>
#include <stdlib.h>    // malloc, free
#include <wchar.h>     // wcslen

#pragma comment(lib, "cfgmgr32.lib")

//
// Opens and closes the disk using its device interface path.
// Zero desired access is intentional: this sample does not read or write data.
// When extending it, request the access required by the intended operation:
// GENERIC_READ for reads, GENERIC_WRITE for writes, and the access required
// by the specific IOCTL. Applicable device permissions also apply.
//
static void
ProcessDisk(
    const wchar_t* DevicePath
    )
{
    HANDLE handle;

    handle = CreateFileW(
        DevicePath,
        0,  // No data read/write access requested.
        FILE_SHARE_READ | FILE_SHARE_WRITE,
        NULL,
        OPEN_EXISTING,
        0,
        NULL
        );

    if (handle == INVALID_HANDLE_VALUE)
    {
        wprintf(L"  open failed (%lu): %s\n", GetLastError(), DevicePath);
        return;
    }

    // TODO: perform a supported query whose access requirements are satisfied
    // by this handle. Adjust the CreateFileW access argument before adding
    // operations that require read or write access.

    CloseHandle(handle);
}

int
wmain(
    void
    )
{
    wchar_t* list;
    CONFIGRET cr;
    ULONG len;
    DWORD index;

    len = 0;

RetryEnumeration:
    //
    // Select currently enabled disk device interfaces.
    // This does not indicate the disk's online/offline state.
    //
    cr = CM_Get_Device_Interface_List_SizeW(
        &len,
        (LPGUID)&GUID_DEVINTERFACE_DISK,
        NULL,
        CM_GET_DEVICE_INTERFACE_LIST_PRESENT
        );

    if (cr != CR_SUCCESS || len == 0)
    {
        wprintf(L"CM_Get_Device_Interface_List_SizeW failed: 0x%lx\n", cr);
        return 1;
    }

    //
    // The result is a REG_MULTI_SZ style buffer: a contiguous run of
    // NUL-terminated device paths, terminated by an extra empty string.
    // 'len' is expressed in characters (including all NULs), so size the
    // allocation in wchar_t units, not bytes.
    //
    list = (wchar_t*)malloc((size_t)len * sizeof(wchar_t));

    if (list == NULL)
    {
        wprintf(L"Out of memory allocating %lu characters\n", len);
        return 1;
    }

    cr = CM_Get_Device_Interface_ListW(
        (LPGUID)&GUID_DEVINTERFACE_DISK,
        NULL,
        list,
        len,
        CM_GET_DEVICE_INTERFACE_LIST_PRESENT
        );

    if (cr == CR_BUFFER_SMALL)
    {
        // An interface may have arrived after the size query.
        free(list);
        goto RetryEnumeration;
    }

    if (cr != CR_SUCCESS)
    {
        wprintf(L"CM_Get_Device_Interface_ListW failed: 0x%lx\n", cr);
        free(list);
        return 1;
    }

    //
    // Walk the multi-string buffer, one NUL-terminated device path per
    // iteration, stopping at the empty string that terminates the list.
    // 'list' is guaranteed NUL-terminated by the API contract, so this
    // cannot run past the allocation.
    //
    index = 0;

    for (wchar_t* current = list; *current != L'\0'; current += wcslen(current) + 1)
    {
        wprintf(L"[%lu] %s\n", index, current);
        ProcessDisk(current);
        index++;
    }

    free(list);
    return 0;
}
```

## Related content

- [Enumerating installed device interfaces](/windows-hardware/drivers/install/enumerating-installed-device-interface-classes)
- [CM_Get_Device_Interface_ListW](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_listw)
- [CM_Get_Device_Interface_List_SizeW](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_list_sizew)
- [IOCTL_STORAGE_GET_DEVICE_NUMBER](/windows/win32/api/winioctl/ni-winioctl-ioctl_storage_get_device_number)
- [IOCTL_STORAGE_QUERY_PROPERTY](/windows/win32/api/winioctl/ni-winioctl-ioctl_storage_query_property)
- [GUID_DEVINTERFACE_DISK](/windows-hardware/drivers/install/guid-devinterface-disk)
- [IoGetDeviceInterfaces (kernel-mode equivalent)](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces)
- [CreateFileW: requested access rights](/windows/win32/api/fileapi/nf-fileapi-createfilew)
- [Defining I/O control codes: guidance for setting the Access bits](/windows-hardware/drivers/kernel/defining-i-o-control-codes#guidance-for-setting-the-access-bits)
- [CM_Register_Notification: registration ordering and initial enumeration](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification)
