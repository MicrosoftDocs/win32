---
Description: 'Commands are special jobs that contain a single task. A command job is not scheduled (it runs immediately) and can be run only by administrators.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1483a9b8-58e9-4925-85bc-133575b6171b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Executing Commands
---

# Executing Commands

Commands are special jobs that contain a single task. A command job is not scheduled (it runs immediately) and can be run only by administrators. The specified command must exist on all nodes on which it is to run. By default, the command runs on all nodes in the cluster; however, you can limit it to run on a specified list of nodes.

To create a command, call the [**IScheduler::CreateCommand**](ischeduler-createcommand.md) method. If the command requires specific environment variables, standard input from a file, or must be launched in a specific directory, use the [**ICommandInfo**](icommandinfo.md) interface to specify these requirements.

To start the command, call one of the following methods:

-   [**Start**](iremotecommand-start.md)
-   [**StartWithCredentials**](iremotecommand-startwithcredentials.md)

With the [**Start**](iremotecommand-start.md) method, the user provides the credentials. With the [**StartWithCredentials**](iremotecommand-startwithcredentials.md) method, the user name and password are specified. If the password is not specified, the user provides the password unless the credentials have been cached.

> [!Note]  
> After starting the command, your application must continue to run until the job that run the command finishes. If your application exits too soon, the HPC Job Scheduler Service may not create and start the task that runs the command.

 

The command provides the following events to which you may subscribe:

-   [**OnCommandOutput**](iremotecommandevents-oncommandoutput.md)
-   [**OnCommandRawOutput**](iremotecommandevents-oncommandrawoutput.md)
-   [**OnCommandTaskState**](iremotecommandevents-oncommandtaskstate.md)
-   [**OnCommandJobState**](iremotecommandevents-oncommandjobstate.md)

To receive notification when the state of the job that contains the command changes, subscribe to the [**OnCommandJobState**](iremotecommandevents-oncommandjobstate.md) event. To receive notification when the state of the command changes on a node, subscribe to the [**OnCommandTaskState**](iremotecommandevents-oncommandtaskstate.md) event. To receive each line of output as it is generated on a node, subscribe to the [**OnCommandOutput**](iremotecommandevents-oncommandoutput.md) event. The [**OnCommandRawOutput**](iremotecommandevents-oncommandrawoutput.md) event is similar to **OnCommandOutput** except that the output is a byte blob that contains the output as the command writes it (the output could contain one or more lines or be a partial line of output). Note that these callbacks do not block the command from continuing; by the time you handle the notification, the state of the job or task may have already transitioned to a new state.

The following example shows how to create and run a command and how to subscribe to events in C#. For an example that implements the event handler for the events, see [Implementing the Event Handlers for Command Events in C#](implementing-the-event-handlers-for-command-events-in-c-.md).


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading;
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;


namespace CommandWithDelegates
{
    class Program
    {
        private static ManualResetEvent manualEvent = new ManualResetEvent(false);

        static void Main(string[] args)
        {
            IScheduler scheduler = new Scheduler();
            IRemoteCommand command = null;
            IStringCollection nodes = null;

            try
            {
                scheduler.Connect("localhost");

                if (UserPrivilege.Admin == scheduler.GetUserPrivilege())
                {
                    // Specify that the command runs on a single node. To specify
                    // more nodes, use the nodes.Add method.
                    nodes = scheduler.CreateStringCollection();
                    nodes.Add("<NODENAMEGOESHERE>");

                    // Create the command.
                    command = scheduler.CreateCommand(@"<COMMANDGOESHERE>", null, nodes);

                    // Subscribe to one or more events before starting the command.
                    command.OnCommandJobState += JobStateCallback;
                    command.OnCommandTaskState += TaskStateCallback;
                    command.OnCommandOutput += OutputCallback;
                    command.OnCommandRawOutput += RawOutputCallback;

                    // Run the command.
                    command.StartWithCredentials(@"<domain\username>", null);

                    // Blocks so that the events get delivered. One of your event
                    // handlers need to set this event.
                    manualEvent.WaitOne();

                    Console.Write("\nPress Enter to quit");
                    Console.ReadLine();
                }
                else
                {
                    Console.WriteLine("You must run as an administrator to create commands.");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        // Add the code from the Implementing the Event Handlers for Command Events in C# topic here.

```

<span codelanguage="CSharp"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C#</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>    }
}</code></pre></td>
</tr>
</tbody>
</table>



The following example shows how to create and run a command and how to subscribe to events in C++. If you subscribe to events, you will receive all events (you cannot subscribe to individual events). If you do not want to handle an event, your implementation for the event should simply return. For an example that implements the event handler for the events, see [Implementing the Event Handlers for Command Events in C++](implementing-the-event-handlers-for-command-events-in-c--.md). This example assumes that the *pScheduler* variable is a valid pointer to an [**IScheduler**](ischeduler.md) instance.


```C++
// Created in RunCommand and set in CCommandEventHandler::OnCommandJobState
// when the state of the job changes to Finished, Failed, or Canceled.
HANDLE g_CommandDoneEvent = NULL;

```

<span codelanguage="ManagedCPlusPlus"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>void RunCommand(IScheduler* pScheduler)
{
    HRESULT hr = S_OK;
    IRemoteCommand* pCommand = NULL;
    IConnectionPointContainer* pCPContainer = NULL;
    static IConnectionPoint* pConnectionPoint = NULL;
    IStringCollection* pNodes = NULL;
    static DWORD cookie = 0;
    CCommandEventHandler *pHandler = NULL;
    IUnknown* punk = NULL;
    UserPrivilege PrivilegeLevel;

    hr = pScheduler-&gt;GetUserPrivilege(&amp;PrivilegeLevel);
    if (FAILED(hr))
    {
        wprintf(L&quot;pScheduler-&gt;GetUserPrivilege failed with 0x%x\n&quot;, hr);
        goto cleanup;
    }

    // Check the privilege level of the user. To run commands, the user must be 
    // running as an elevated administrator.
    if (UserPrivilege_Admin == PrivilegeLevel)
    {
        hr = pScheduler-&gt;CreateCommand(_bstr_t(L&quot;&lt;COMMANDGOESHERE&gt;&quot;), NULL, NULL, &amp;pCommand);
        if (FAILED(hr))
        {
            wprintf(L&quot;pScheduler-&gt;CreateCommand failed with 0x%x\n&quot;, hr);
            goto cleanup;
        }

        // To subscribe to events, you need to get the connection point container and then
        // find the connection point for the IRemoteCommandEvents interface.
        hr = pCommand-&gt;QueryInterface(__uuidof(IConnectionPointContainer), reinterpret_cast&lt;void **&gt; (&amp;pCPContainer));
        if (FAILED(hr))
        {
            wprintf(L&quot;pCommand-&gt;QueryInterface(__uuidof(IConnectionPointContainer) failed with 0x%x\n&quot;, hr);
            goto cleanup;
        }

        hr = pCPContainer-&gt;FindConnectionPoint(__uuidof(IRemoteCommandEvents), &amp;pConnectionPoint);
        if (FAILED(hr))
        {
            wprintf(L&quot;pCPContainer-&gt;FindConnectionPoint failed with 0x%x\n&quot;, hr);
            goto cleanup;
        }

        // Create an instance of your event handler implementation.
        pHandler = new CCommandEventHandler();

        if (pHandler)
        {
            // Get the IUnknown interface for your implementation and pass it to the Advise method.
            hr = pHandler-&gt;QueryInterface(__uuidof(IUnknown), reinterpret_cast&lt;void **&gt; (&amp;punk));

            // Subscribe to the events that the RemoteCommand object fires.
            // Use the cookie when done to remove the subscription.
            hr = pConnectionPoint-&gt;Advise(punk, &amp;cookie);
            if (FAILED(hr))
            {
                wprintf(L&quot;pConnectionPoint-&gt;Advise failed with 0x%x\n&quot;, hr);
                goto cleanup;
            }
        }
        else
        {
            wprintf(L&quot;Failed to instantiate CCommandEventHandler\n&quot;);
        }

        g_CommandDoneEvent = CreateEvent (NULL, TRUE, FALSE, NULL);

        // Run the command.
        hr = pCommand-&gt;StartWithCredentials(_bstr_t(L&quot;&lt;domain\\username&gt;&quot;), NULL);
        if (FAILED(hr))
        {
            wprintf(L&quot;pCommand-&gt;StartWithCredentials failed with 0x%x\n&quot;, hr);
            goto cleanup;
        }

        // Loop while the command is running. Stop when the command finishes, fails,
        // or is canceled. The wait object is set in the CCommandEventHandler::OnCommandJobState
        // callback.
        while (true)
        {
            DWORD dwWait = MsgWaitForMultipleObjects (
                1, &amp;g_CommandDoneEvent, FALSE, INFINITE, QS_ALLINPUT);

            if (dwWait == WAIT_OBJECT_0)
            {
                wprintf(L&quot;\nCommand finished\n&quot;);
                goto cleanup;
            }
            else if (dwWait == WAIT_OBJECT_0 + 1)
            {
                MSG msg;  
                while (PeekMessage(&amp;msg, NULL, 0, 0, PM_REMOVE)) 
                { 
                    DispatchMessage(&amp;msg); 
                } 

            }
        }
    }
    else
    {
        wprintf(L&quot;User must be running application with administrator privileges.\n&quot;);
    }

cleanup:

    if (pCommand)
        pCommand-&gt;Release();

    if (pHandler)
        pHandler-&gt;Release();

    if (punk)
        punk-&gt;Release();

    if (pCPContainer)
        pCPContainer-&gt;Release();

    if (pConnectionPoint)
    {
        if (cookie)
            hr = pConnectionPoint-&gt;Unadvise(cookie);

        pConnectionPoint-&gt;Release();
    }
}</code></pre></td>
</tr>
</tbody>
</table>



 

 



