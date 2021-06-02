---
description: Windows 8 and Windows Server 2012 introduce the ability for software that is running on a virtual machine to detect that a time shift event may have occurred.
ms.assetid: 0793E46B-8464-425E-8C5B-77C14DA90004
title: Virtual machine generation identifier
ms.topic: article
ms.date: 05/31/2018
---

# Virtual machine generation identifier

Windows 8 and Windows Server 2012 introduce the ability for software that is running on a virtual machine to detect that a time shift event may have occurred. Time shift events can occur as a result of an application of a virtual machine snapshot or the restoration of a virtual machine backup. For more information about this functionality, see the [Virtual Machine Generation ID white paper](https://download.microsoft.com/download/3/1/C/31CFC307-98CA-4CA5-914C-D9772691E214/VirtualMachineGenerationID.docx).

## Prerequisites

To use the virtual machine generation identifier from inside a virtual machine your virtual machine must conform to the following.

-   The virtual machine must be running on a hypervisor that implements support for virtual machine generation identifiers. Currently, these are the following:
    -   Windows 8
    -   Windows Server 2012
    -   Microsoft Hyper-V Server 2012
-   The virtual machine must be running a guest operating system that has support for the virtual machine generation identifier. Currently, these are the following.

    The following operating systems have native support for the virtual machine generation identifier.

    -   Windows 8
    -   Windows Server 2012
    -   

    The following operating can be used as the guest operating system if the Hyper-V integration services from Windows 8 or Windows Server 2012 are installed.

    -   Windows Server 2008 R2 with Service Pack 1 (SP1)
    -   Windows 7 with Service Pack 1 (SP1)
    -   Windows Server 2008 with Service Pack 2 (SP2)
    -   Windows Server 2003 R2
    -   Windows Server 2003 with Service Pack 2 (SP2)
    -   Windows Vista with Service Pack 2 (SP2)
    -   Windows XP with Service Pack 3 (SP3)

## Obtaining the virtual machine generation identifier

To programmatically obtain the virtual machine generation identifier, perform the following steps.

> [!Note]  
> The following must be run with administrator or system privileges to function correctly.

 

1.  Include header file "vmgenerationcounter.h" in your app. The header file contains these definitions:
    ```C++
    DEFINE_GUID(
        GUID_DEVINTERFACE_VM_GENCOUNTER,
        0x3ff2c92b, 
        0x6598, 
        0x4e60, 
        0x8e, 
        0x1c, 
        0x0c, 
        0xcf, 
        0x49, 
        0x27, 
        0xe3, 
        0x19);

    #define VM_GENCOUNTER_SYMBOLIC_LINK_NAME L"VmGenerationCounter"

    #define IOCTL_VMGENCOUNTER_READ CTL_CODE( \
        FILE_DEVICE_ACPI, \
        0x1, METHOD_BUFFERED, \
        FILE_READ_ACCESS | FILE_WRITE_ACCESS)

    typedef struct _VM_GENCOUNTER
    {
        ULONGLONG GenerationCount;
        ULONGLONG GenerationCountHigh;
    } VM_GENCOUNTER, *PVM_GENCOUNTER;
    ```

    

2.  Open a handle to the "\\\\.\\VmGenerationCounter" device using the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function. Alternatively, you can use the PnP manager to consume the device interface **GUID\_DEVINTERFACE\_VM\_GENCOUNTER** ({3ff2c92b-6598-4e60-8e1c-0ccf4927e319}). These objects will not be present if the app is not running in a virtual machine.
3.  Send the [**IOCTL\_VMGENCOUNTER\_READ**](/windows/desktop/api/Vmgenerationcounter/ni-vmgenerationcounter-ioctl_vmgencounter_read) IOCTL to the driver to retrieve the generation identifier.

    The [**IOCTL\_VMGENCOUNTER\_READ**](/windows/desktop/api/Vmgenerationcounter/ni-vmgenerationcounter-ioctl_vmgencounter_read) IOCTL operates in one of two modes, *polling*, and *event driven*.

    To issue the IOCTL in polling mode, you submit the IOCTL with an input buffer of zero length. In response to this, the driver retrieves the current generation identifier, writes it to the output buffer, and completes the IOCTL.

    To issue the IOCTL in event driven mode, submit the IOCTL with an input buffer that contains an existing generation identifier. In response to this, the driver waits until the current generation identifier becomes different from the generation identifier that was passed in. When the generation identifier changes, the driver writes the current generation identifier to the output buffer and completes the IOCTL.

    In both modes, the format and length of the output buffer is dictated by the [**VM\_GENCOUNTER**](/windows/desktop/api/Vmgenerationcounter/ns-vmgenerationcounter-vm_gencounter) structure.

    Polling mode is supported on all of the guest operating systems listed above. Event driven mode is supported only on Windows Vista with SP2, Windows Server 2008 with SP2, and later operating systems. On earlier operating systems, the IOCTL will fail with the error code **ERROR\_NOT\_SUPPORTED** when issued in event driven mode.

    It is possible for the generation identifier to change between the time that it is retrieved by the driver and the time the IOCTL is completed. This can result in the client app receiving stale data. To avoid this, the client app can use event driven mode to ensure that it will eventually learn about any updates to the generation identifier. By taking the client app's current identifier as input, event driven mode avoids potential race conditions that would cause the caller to miss notifications.

The following code example shows how to perform the above actions to obtain the virtual machine generation identifier.

> [!Note]  
> The following code must be run with administrator or system privileges to function correctly.

 


```C++
HRESULT GetVmCounter(bool fWaitForChange)
{
    BOOL success = FALSE;
    DWORD error = ERROR_SUCCESS;
    VM_GENCOUNTER vmCounterOutput = {0};
    DWORD size = 0;
    HANDLE handle = INVALID_HANDLE_VALUE;
    HRESULT hr = S_OK;

    handle = CreateFile(
        L"\\\\.\\" VM_GENCOUNTER_SYMBOLIC_LINK_NAME,
        GENERIC_READ | GENERIC_WRITE,
        FILE_SHARE_READ | FILE_SHARE_WRITE,
        NULL,
        OPEN_EXISTING,
        0,
        NULL);

    if (handle == INVALID_HANDLE_VALUE)
    {
        error = GetLastError();

        wprintf(
            L"Unable to open device %s. Error code = %d.", 
            VM_GENCOUNTER_SYMBOLIC_LINK_NAME, 
            error);

        hr = HRESULT_FROM_WIN32(error);

        goto Cleanup;
    }

    /*
    Call into the driver. 

    Because the 4th parameter to DeviceIoControl (nInBufferSize) is zero, this 
    is a polling request rather than an event-driven request.
    */
    success = DeviceIoControl(
        handle,
        IOCTL_VMGENCOUNTER_READ,
        NULL,
        0,
        &vmCounterOutput,
        sizeof(vmCounterOutput),
        &size,
        NULL);

    if (!success)
    {
        error = GetLastError();

        wprintf(L"Call IOCTL_VMGENCOUNTER_READ failed with %d.", error);

        hr = HRESULT_FROM_WIN32(error);

        goto Cleanup;
    }

    wprintf(
        L"VmCounterValue: %I64x:%I64x",
        vmCounterOutput.GenerationCount,
        vmCounterOutput.GenerationCountHigh);

    if (fWaitForChange)
    {
        /*
        Call into the driver again in event-driven mode. DeviceIoControl won't 
        return until the generation identifier has changed.
        */
        success = DeviceIoControl(
            handle,
            IOCTL_VMGENCOUNTER_READ,
            &vmCounterOutput,
            sizeof(vmCounterOutput),
            &vmCounterOutput,
            sizeof(vmCounterOutput),
            &size,
            NULL);

        if (!success)
        {
            error = GetLastError();

            wprintf(L"Call IOCTL_VMGENCOUNTER_READ failed with %d.", error);

            hr = HRESULT_FROM_WIN32(error);

            goto Cleanup;
        }

        wprintf(
            L"VmCounterValue changed to: %I64x:%I64x",
            vmCounterOutput.GenerationCount,
            vmCounterOutput.GenerationCountHigh);
    }

Cleanup:

    if (handle != INVALID_HANDLE_VALUE)
    {
        CloseHandle(handle);
    }

    return hr;
};
```



## Determining if a time shift event has occurred

After you have obtained the virtual machine generation identifier, you should store it for future use. Before your app performs a time-sensitive operation, such as committing to a database, you should re-obtain the generation identifier and compare it to the stored value. If the identifier has changed, that means that a time shift event has occurred, and your app must act appropriately.

 

 
