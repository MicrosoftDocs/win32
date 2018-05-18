---
title: Image File Execution Options
description: Image File Execution Options
ms.assetid: '585ac744-f7e2-4e9d-aca5-d50642535da3'
---

# Image File Execution Options

Image File Execution Options (IFEO) are often used to turn on debugging automatically when starting a process by setting appropriate registry value for the "Tracing Flags" options. At process load time "Tracing Flags" registry entry is read. If the value is non-zero, the bits are ORed into the appropriate DWORD in the PEB. The values to be set are:


```
Heap Tracing Enabled  Ox00000001
CritSecTracingEnabled 0x00000002
```



After the "Tracing Flags" options are set heap tracing is turned on in the kernel. In the accompanying example this is accomplished by turning heap tracing "On" for process PID=0. This process is used for two reasons, it always exists and it does not do heap allocations.

The trace is stopped and merged in the usual manner as shown in the example.

> [!Note]  
> Certain WPA features can only support heap tracing for 1 or 2 processes, while other features do not have a limit. Heap graphs and summary tables do not have a limit.

 


```
@rem Update the Image File Execution key.
reg add    "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SearchIndexer.exe"      /v TracingFlags /t REG_DWORD /d 1 /f
reg add    "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SearchProtocolHost.exe" /v TracingFlags /t REG_DWORD /d 1 /f
reg add    "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SearchFilterHost.exe"   /v TracingFlags /t REG_DWORD /d 1 /f
reg query  "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" /s /v TracingFlags

Net stop WSearch

xperf -on base+FileIo+Virt_Alloc -stackwalk VirtualAlloc -buffersize 64 -minbuffers 100 -maxbuffers 300 -f \tmpKernel.etl 

@rem Turn on flag in kernel to do heap tracing.
xperf -start HeapSession -heap -Pids 0 -stackwalk HeapCreate+HeapAlloc+HeapRealloc -BufferSize 64 -MinBuffers 700 -MaxBuffers 700 -f \tmpHeap.etl


Net start WSearch

@choice /t:60 /D y > NUL

xperf -stop "NT Kernel Logger" -stop HeapSession -d MyTrace.etl


@rem Clean up registry flags.

reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SearchIndexer.exe"      /v TracingFlags /f
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SearchProtocolHost.exe" /v TracingFlags /f
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SearchFilterHost.exe"   /v TracingFlags /f
reg query  "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" /s /v TracingFlags
```



 

 




