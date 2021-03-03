---
title: system_handle attribute
description: The \ system_handle\ attribute specifies a system-defined handle type.
keywords:
- system_handle attribute MIDL
topic_type:
- apiref
api_name:
- system_handle
api_type:
- NA
ms.topic: reference
ms.date: 02/05/2021
---

# system_handle attribute

The \[**system_handle**\] attribute specifies a system-defined handle type that represents access to a system object.

``` syntax
[system_handle(system-handle-type[,optional-access-mask])]
```

## Parameters

<dl> <dt>

*system-handle-type* 
</dt> <dd>

Specifies one of the system handle type options.

The valid options are:
* [sh_composition](sh-composition.md) - A DirectComposition surface handle
* [sh_event](sh-event.md) - A named or unnamed event object
* [sh_file](sh-file.md) - A file or I/O device
* [sh_job](sh-job.md) - A job object
* [sh_mutex](sh-mutex.md) - A named or unnamed mutex object
* [sh_pipe](sh-pipe.md) - An anonymous or named pipe object
* [sh_process](sh-process.md) - A process object
* [sh_reg_key](sh-reg-key.md) - A registry key
* [sh_section](sh-section.md) - A shared memory section
* [sh_semaphore](sh-semaphore.md) - A named or unnamed semaphore object
* [sh_socket](sh-socket.md) - A WinSock socket object
* [sh_thread](sh-thread.md) - A thread object
* [sh_token](sh-token.md) - An access token object

</dd> <dt>

*optional-access-mask*
</dt> <dd>

Optionally requests specific access rights applied to the duplicated handle. By default when this is unspecified, the handle will be duplicated with the same access. 

To specify a different level of access, use object specific access rights corresponding to the underlying system object selected.

More information on how access rights are propagated during duplication can be found on the [DuplicateHandle](/windows/win32/api/handleapi/nf-handleapi-duplicatehandle) documentation.

Links to lists of access rights for each type of object can be found in the *DuplicateHandle* reference as well as in the **See also** headings of each `sh_*` parameter page.

</dd> </dl>

## Remarks

In order to use this attribute, the `-target` flag must be set to `NT100` (or higher) when running midl.exe.

System handles are handles that are defined by the operating system to provide access to a system resource. The specific type of the object behind the handle must be specified when declaring the attribute.

For a handle marked `[in]`, the handle will be duplicated into the remote procedure and remains valid for the duration of that procedure. On return from the remote procedure, the duplicated handle is freed. To maintain access to the underlying object, the remote application must duplicate the handle into its own address space.

By contrast, for a handle marked `[out]`, when a remote procedure returns a handle from a call, the remote procedure will lose ownership of it. To maintain access to the underlying object, the remote procedure should duplicate the handle and return the duplicate. The returned handle then becomes owned by the caller who assumes a responsibility to close it when access to the underlying system object is no longer necessary.

As this is a mechanism for relaying access to a system object, this attribute is only applicable to calls between procedures on the same machine.

The creation and access parameters given to the underlying object behind the system handle on its creation will dictate whether it can be successfully marshalled to the remote procedure context.

An array of `system_handle` can be passed either in or out with the syntax found in the [**size_is attribute**](size-is.md) documentation.

## Examples

The following examples several uses of `system_handle`. For a complete sample, see the [SystemHandlePassing](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/SystemHandlePassing) sample.

```c
interface MyInterface : IUnknown                         
{         
    HRESULT Proc1([in, system_handle(sh_file)] HANDLE writeThisFile);

    HRESULT Proc2([in, system_handle(sh_pipe, FILE_GENERIC_READ)] HANDLE readThisPipe);

    HRESULT Proc3([out, system_handle(sh_composition)] HANDLE* visual);

    HRESULT Proc4([in] DWORD cEvents, [out, system_handle(sh_event), size_is(cEvents)] HANDLE* pWatchAllTheseEvents);
}
```

## Requirements

| &nbsp; | &nbsp; |
|-|-|
| Minimum supported client | Windows 10 Anniversary Update (version 1607, build 14393) |
| Minimum supported server | Windows Server 2016 (build 14393) |

## See also

<dl> <dt>
<!--
[System Handle Passing sample code](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/SystemHandlePassing)
</dt> <dt>
-->

[/target switch](./-target.md)
</dt> <dt>

[Binding and Handles](../Rpc/binding-and-handles.md)
</dt> <dt>

[Handles and Objects](../sysinfo/handles-and-objects.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**DuplicateHandle**](/windows/win32/api/handleapi/nf-handleapi-duplicatehandle)
</dt> <dt>

[Security Descriptors](../secauthz/security-descriptors.md)
</dt></dl>
