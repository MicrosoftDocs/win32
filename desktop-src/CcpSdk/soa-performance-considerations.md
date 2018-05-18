---
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3bd49f68-5ce0-4c93-9d51-ca647c938983'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: SOA Performance Considerations
---

# SOA Performance Considerations

For performance considerations related to service-oriented architecture (SOA), see the following sections:

-   [Thottling requests](#throttling-requests)
-   [Handling large messages](#handling-large-messages)
-   [Reducing the message-passing overhead](#reducing-the-message-passing-overhead)

## Throttling requests

The asynchronous nature of the SOA programming model can lead to large memory usage if the size of the data or the number of messages being passed is very large. The goal of the client should be to maximize the number of concurrent messages that it sends to the broker without overloading the broker.

For a single client running in the cluster, the number of concurrent messages should be equal to the number of cores available using the resource units that you specify. For example, if you specify nodes for the resource units and there are four nodes in the cluster with four cores each, then you should send 16 messages. If the messages are short, consider sending additional messages so that there are always messages available to the broker in the queue.

If you send too many messages, the broker will stop accepting messages. If you send the messages synchronously, the client will block. If you send the messages asynchronously, the client will eventually receive a TimeoutException exception.

To control the memory usage, the client application should throttle or limit the number of outstanding requests that it has sent to the service.

One mechanism for throttling the messages is for the client application to use a semaphore to control the number of outstanding requests that it issues. In the following example, the client application limits the number of outstanding request to 16.


```CSharp
           This example is based on the example in the "Creating a SOA Client" topic.

           // Create a semaphore that can satisfy up to 16 concurrent requests. Use an 
           // initial count of 16 so that initially the sending thread (main program) can 
           // send up to 16 requests.

            Semaphore outstandingRequests = new Semaphore(16, 16);
            
            SessionStartInfo info = new SessionStartInfo(scheduler, serviceName);
            using (Session session = Session.CreateSession(info))
            {
                int i;

                NetTcpBinding binding = new NetTcpBinding(SecurityMode.Transport, false);

                EchoServiceClient client = new EchoServiceClient(binding, session.EndpointReference);

                // Set the time-out to 1 day.
                client.InnerChannel.OperationTimeout = new TimeSpan(1, 0, 0, 0);

                AsyncResultCount = 100;

                // Send 100 messages.
                for (i = 0; i < 100; i++)
                {
                    // This call will block if there are 16 outstanding requests. The thread 
                    // is released when the receiving thread (the EchoCallBack function) calls 
                    // the outstandingRequests.Release method. 
                    outstandingRequests.WaitOne();

                    client.BeginEcho("Hello, world!", EchoCallback, new RequestState(client, i));
                }

                AsyncResultsDone.WaitOne();

                client.Close();

                Console.WriteLine("Please enter any key to continue...");
                Console.ReadLine();
            }
        }

        // Entry point for the receiving thread.
        static void EchoCallback(IAsyncResult result)
        {
            RequestState state = result.AsyncState as RequestState;

            if (Interlocked.Decrement(ref AsyncResultCount) <= 0)
            {
                    AsyncResultsDone.Set();

                return;
            }

            string response = state.GetResult(result);
            Console.WriteLine("Response({0}) = {1}", state.Input, response);
         
            // Signals the sending thread to resume sending requests.
            outstandingRequests.Release();
         }
```



## Handling large messages

The default WCF message size is 64 KB. To send messages larger than 64 KB, you must specify the larger message size that you want to support for both the client application and the service. As an alternative to increasing the message size, consider using a reference to message data instead. For details, see [Reducing the message passing overhead](#reducing-the-message-passing-overhead).

On the client application side, set the buffer size when creating the binding as shown in the following example. You can also set the buffer size in the client configuration file (*client*.exe.config) so that the values are not hardcoded in the application. For details on setting these values, see the NetTcpBinding and BasicHttpBinding classes in the .NET framework.


```CSharp
    NetTcpBinding binding = new NetTcpBinding(SecurityMode.Transport);

    binding.MaxBufferSize = 262144;
    binding.MaxReceivedMessageSize = 262144;
    binding.MaxBufferPoolSize = 1048576;
    binding.ReaderQuotas.MaxArrayLength = 131072;
    binding.ReaderQuotas.MaxBytesPerRead = 262144;

    Service1Client client = new Service1Client(binding, session.EndpointReference);
```



On the service side, specify the message size in the service's configuration file that you create as shown in the following example. The configuration file is named, *service\_DLL\_file\_name*.dll.config and must exist in the same folder as your service DLL.

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.serviceModel>
    <bindings>
      <!-- configure a binding that support a session -->
      <netTcpBinding>
        <binding name="myBinding" portSharingEnabled="true" maxReceivedMessageSize="262144">
          <readerQuotas maxArrayLength="1048576"/>
          <security mode="Transport"/>
        </binding>
      </netTcpBinding>
    </bindings>
    
    <services>
      <service name="EchoService.EchoService">
        <endpoint address="" binding="netTcpBinding" bindingConfiguration="myBinding" contract="EchoService.IEchoService"/>
      </service>
    </services>
  </system.serviceModel>
</configuration>
```

## Reducing the message-passing overhead

Although you can configure the client and service to process messages greater than the default size of 64 KB, you should consider other alternatives because larger objects lead to long serialization times. Depending on the underlying processor speed and memory architecture, there is a point beyond which sending larger messages yields diminishing returns with respect to the network bandwidth. Adding cores to the session does not reduce the processing time.

To reduce the size of the messages, the developer can send references to the object instead. By enabling the service to load the data, the developer can avoid sending large objects via the broker, thus avoiding the serialization time associated with the WCF stack. Moreover, because parametric sweep applications typically access shared global data, directing the client application to cache the global data and having the services load the data at startup eliminates further data transfer costs — the client application sends only processing-specific data, as opposed to duplicating the global data in each request.

 

 



