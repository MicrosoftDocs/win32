---
title: Operation Recorder
description: .
ms.assetid: c1051b62-0e67-4480-81c6-cb138d3296d6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Operation Recorder

## Purpose

Operation Recorder enables applications to speed up operations that repeatedly access the same file data by exposing the Windows prefetching mechanism as a public interface.

## Developer audience

Operation Recorder is designed for use by C/C++ developers of Windows applications. The operation recorder API enables applications to use prefetching in run time scenarios other than application launch.

## Run-time requirements

On Windows 8, this functionality requires the Superfetch service to be enabled. Windows 8 will have the service enabled by default. For Windows Server 2012, this prefetching functionality needs to be enabled and disabled as required. This can be done using CIM based PowerShell cmdlets. The prefetcher functionality can be exposed using the [CIM class](https://msdn.microsoft.com/library/aa386179) : **CIM\_PrefetcherService**.

## Related topics

<dl> <dt>


</dt> <dt>

[**OperationStart**](/windows/win32/WinBase/nf-winbase-operationstart?branch=master)
</dt> <dt>

[**OperationEnd**](/windows/win32/WinBase/nf-winbase-operationend?branch=master)
</dt> <dt>

[**OPERATION\_START\_PARAMETERS**](/windows/win32/WinBase/ns-winbase-_operation_start_parameters?branch=master)
</dt> <dt>

[**OPERATION\_END\_PARAMETERS**](/windows/win32/WinBase/ns-winbase-_operation_end_parameters?branch=master)
</dt> <dt>

[**OPERATION\_ID**](operation-id.md)
</dt> </dl>

 

 




