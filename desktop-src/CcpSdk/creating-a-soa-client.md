---
Description: 'HPC sessions support SOA-based clients. To create an HP session from your client, call the Session.CreateSession or Session.BeginCreateSession method.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '99ab7d3f-beed-4f96-98d4-51a8d54080ca'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Creating a SOA Client
---

# Creating a SOA Client

HPC sessions support SOA-based clients. To create an HP session from your client, call the [Session.CreateSession](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.session.createsession.aspx) or [Session.BeginCreateSession](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.session.begincreatesession.aspx) method. You must create a [SessionStartInfo](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.aspx) class object that specifies the name of the head node of the cluster to connect to and the name of the service's configuration file (specify the name only, not the extension).

The default values for the session properties create a secured, non-shared session that uses NetTcp binding and runs the jobs of the session under the credentials of the user who runs the SOA client application. The scheduler uses nodes to schedule the service instances in the cluster. To specify different session values, use the [SessionStartInfo](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.aspx) class.

**Note**  If you use the [SessionStartInfo.Username](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.username.aspx) property to specify that the jobs for the session run under the credentials of a different user than the user who is the owner for the jobs, the user under whose credentials the jobs run must be an administrator. If that user is not an administrator, an exception occurs because that user does not have permission to read the jobs. The owner for the jobs is the user who runs the SOA client application.

If the user you specify with [SessionStartInfo.Username](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.username.aspx) is the same as the user who owns the jobs, then that user does not need to be an administrator.

After creating the session, use the endpoint reference for the transport scheme that you specified when you created the session, to bind your client proxy to the HPC broker. You can then use the client proxy to call the service's methods.

For performances considerations, see [SOA Performance Considerations](soa-performance-considerations.md).

The following example shows how to create a session and bind the client to the service. In the following code sample, EchoServiceClient refers to a client proxy for EchoService (described in [Creating a SOA Service](creating-a-soa-service.md)).


```CSharp
using System;
using System.Collections.Generic;
using System.Text;
using System.ServiceModel;
using System.Threading;
using Microsoft.Hpc.Scheduler.Session;
using Microsoft.Hpc.Scheduler.Properties;

namespace EchoClient
{
    class Program
    {
        // Note: This example contains code that is specific to Windows HPC Server 2008 R2.
        // Code for Windows HPC Server 2008 is provided but commented out below. To use this
        // example with Windows HPC Server 2008, comment out or delete the Windows HPC Server
        // 2008 R2 code and uncomment the Windows HPC Server 2008 code where noted below.

        static int AsyncResultCount = 0;
        static AutoResetEvent AsyncResultsDone = new AutoResetEvent(false);

        static void Main(string[] args)
        {
            string scheduler = "localhost";       // Name of the head node of the cluster that you want to connect to.
            string serviceName = "EchoService";   // The name of the registration configuration file for
                                                  // the service that you want to send requests to.

            if (args.Length > 0)
            {
                scheduler = args[0];
            }

            // The SessionStartInfo object specifies the head node to connect to and the name of
            // the service to use. You can also use its properties to change the default job properties.
            // Typically, you use it to change the type and number of compute resources to use. You
            // also use it to set the ShareSession property to share the session with others.

            SessionStartInfo info = new SessionStartInfo(scheduler, serviceName);
            // The following line of code is specific to 
            // Windows HPC Server 2008 R2.
            info.ResourceUnitType = JobUnitType.Node;
            
            // To use this example with 
            // Windows HPC Server 2008, comment out the
            // above line and uncomment out the following
            // line.
            // info.SessionResourceUnitType = SessionUnitType.Node; 
                        
            info.MinimumUnits = 1;
            info.MaximumUnits = 4;
           
            Console.WriteLine("Creating a session...");

            // Create the session.
            using (Session session = Session.CreateSession(info))
            {
                Console.WriteLine("Session's Endpoint Reference: {0}", session.EndpointReference.ToString());
                
                // Binds the session to the client proxy using NetTcp binding. The security mode 
                // must be Transport and you cannot enable reliable sessions. To generate the proxy, 
                // run the Visual Studio command SvcUtil.exe.

                // If SessionStartInfo.Secure is false, use SecurityMode.None for NetTcpBinding.
 
                // If you specify more than one transport scheme when you create the session, use the
                // session.HttpEnpointReference or session.NetTcpEndpointReference properties instead 
                // of using session.EndpointReference.

                NetTcpBinding binding = new NetTcpBinding(SecurityMode.Transport, false);

                EchoServiceClient client = new EchoServiceClient(binding, session.EndpointReference);

                // By default, an operation must complete in 60 seconds. Set the time-out as 
                // appropriate for your client. This example sets the time-out to 1 day.
                client.InnerChannel.OperationTimeout = new TimeSpan(1, 0, 0, 0);

                // Use this count to determine when each of the 100 requests has been received;
                // the count is decremented in EchoCallback each time a response is processed. 
                // When all the responses have been received, the main thread is released.

                AsyncResultCount = 100;

                // Send 100 asynchronous messages. The results are sent to the 
                // EchoCallback callback function.
                for (int i = 0; i < 100; i++)
                {
                    client.BeginEcho("Hello, world!", EchoCallback, new RequestState(client, i));
                }

                AsyncResultsDone.WaitOne();   // Blocks until all 100 messages have been processed.

                // You must call Close before Dispose to ensure that statistics for the broke job
                // (for example, JobPropertyIds.CallsPerSecond and JobPropertyIds.CallDuration) 
                // are saved to the store.
                client.Close();

                Console.WriteLine("Please enter any key to continue...");
                Console.ReadKey();
            }
        }


        // Encapsulates the context of the function callback
        class RequestState
        {
            int input;
            EchoServiceClient client;

            public RequestState(EchoServiceClient client, int input)
            {
                this.client = client;
                this.input = input;
            }

            public int Input
            {
                get { return input; }
            }

            public string GetResult(IAsyncResult result)
            {
                return client.EndEcho(result);
            }
        }


        // Processes the responses to the asynchronous requests.
        static void EchoCallback(IAsyncResult result)
        {
            RequestState state = result.AsyncState as RequestState;

            Console.WriteLine("Response({0}) = {1}", state.Input, state.GetResult(result));


            if (Interlocked.Decrement(ref AsyncResultCount) <= 0)
            {
                AsyncResultsDone.Set();
            }
        }
    }
}
```



> [!Note]
>
> A Window Communication Foundation (WCF) client proxy is a client-application construct that exposes the service operations as methods in the .NET Framework programming language of your choice, such as Visual Basic or Visual C#. WCF represents a WCF service in a form that the client application can use to communicate with the remote service. When you add a service reference to a project in Visual Studio, the WCF objects for the client proxies are created automatically. You can also generate a WCF client by using the [ServiceModel Metadata Utility Tool (Svcutil.exe)](http://go.microsoft.com/fwlink/p/?linkid=139432) (http://go.microsoft.com/fwlink/p/?linkid=139432).

 

 

 



