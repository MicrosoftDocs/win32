---
description: WSDAPI logs contain debugging information that can be used to find the root cause of WSDAPI application failures.
ms.assetid: 28b4c032-1c9a-4b3a-9a6a-2948456572b2
title: Enabling WSDAPI Tracing
ms.topic: article
ms.date: 05/31/2018
---

# Enabling WSDAPI Tracing

WSDAPI logs contain debugging information that can be used to find the root cause of WSDAPI application failures. When tracing is enabled, logging information is stored in an .etl file in a user-specified location. This .etl file can be sent to Microsoft developer support for root cause analysis. For information about contacting support, go to [https://support.microsoft.com](https://support.microsoft.com).

This procedure must be done twice: once on the client, and once on the host.

**To enable WSDAPI tracing**

1.  Using Notepad or another text editor, create a text file with the following text:

    ``` syntax
    "{480217a9-f824-4bd4-bbe8-f371caaf9a0d}" 0xFF 0xFF
    "{649e3596-2620-4d58-a01f-17aefe8185db}" 0xFF 0xFF
    "{96ab095a-9519-4f5c-81ee-c510b0a45463}" 0xFF 0xFF
    "{f9be9c98-10db-4318-bb61-cb0ddea08bf7}" 0xFF 0xFF
    "{db1d0418-105a-4c77-9a25-8f96a19716a4}" 0xFF 0xFF
    "{7e2dbfc7-41e8-4987-bca7-76cadfad765f}" 0xFF 0xFF
    "{8b20d3e4-581f-4a27-8109-df01643a7a93}" 0xFF 0xFF
    "{6d04bf88-60a5-4d02-bc5c-94a20ba490ec}" 0xFF 0xFF
    "{75454210-b231-4fea-b2b4-2cc66d7ae8aa}" 0xFF 0xFF
    "{e176aa66-5cc8-4321-9624-f9c1d2b7bf06}" 0xFF 0xFF
    "{836767a6-af31-4938-b4c0-ef86749a9aef}" 0xFF 0xFF
    ```

2.  Save the text file as `C:\temp\traceguids.txt` and then close the file.
3.  Open an elevated command prompt window.
4.  Run the following command: **logman.exe create trace wsdlog -o c:\\temp\\wsd**
5.  Run the following command: **logman.exe update wsdlog -pf c:\\temp\\traceguids.txt**
6.  Run the following command: **logman.exe start wsdlog**
7.  Reproduce the failure by starting the host and client or by pressing F5 in the Network Explorer.

**To disable WSDAPI tracing**

1.  Open an elevated command prompt window.
2.  Run the following command: **logman.exe stop wsdlog**

Once the application failure has been captured, the \*.etl files can be sent to Microsoft support. These files are located in `C:\temp\wsd_*.etl`.

## Related topics

<dl> <dt>

[WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
</dt> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> <dt>

[https://support.microsoft.com](https://support.microsoft.com)
</dt> </dl>

 

 



