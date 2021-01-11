---
description: Troubleshooting
ms.assetid: e3576161-fc04-47e0-b6b8-75af33fe87ff
title: Troubleshooting
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting

If you are having trouble diagnosing your application errors, refer to the following of troubleshooting tips:

-   Make sure that the Distributed Transaction Coordinator (DTC) is running on all servers.
-   Check network communication by first testing on a local computer to verify that the application works. If you are running TCP/IP on your network, you can use the ping.exe utility to verify that the machines are on the network.
-   Make sure that SQL and DTC are located on the same computer or that the DTC Client Configuration program specifies that the DTC is on another computer. If not, SQLConnect will return an error internally when called from a transactional component.
-   Set the transaction time-out to a higher number than the default 60 seconds. After the transaction time-out has elapsed, COM+ aborts the transaction. All subsequent calls to the component return immediately with CONTEXT\_E\_ABORTED.
-   Make sure that your ODBC drivers are thread-safe and do not have thread affinity.
-   If you have difficulty getting an application to work over several servers, reboot the client and then verify that your domain controller is configured properly.

## Related topics

<dl> <dt>

[Fault Isolation and Failfast Policy](fault-isolation-and-failfast-policy.md)
</dt> <dt>

[Finding the Source of an Error](finding-the-source-of-an-error.md)
</dt> <dt>

[How COM+ Modifies Return Values](how-com--modifies-return-values.md)
</dt> <dt>

[Interpreting Error Codes](interpreting-error-codes.md)
</dt> <dt>

[Strategies for Handling Errors in COM+](strategies-for-handling-errors-in-com-.md)
</dt> </dl>

 

 



