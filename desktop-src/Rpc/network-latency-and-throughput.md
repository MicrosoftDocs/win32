---
title: Network Latency and Throughput
description: Network latency and throughput with Remote Procedure Call (RPC).
ms.assetid: 8285fd73-eb54-4c06-b01a-1bffafb7e675
ms.topic: article
ms.date: 05/31/2018
---

# Network Latency and Throughput

Three major issues relate to optimal use of the network:

-   Network latency
-   Network saturation
-   Packet processing implications

This section introduces a programming task requiring use of RPC, then designs two solutions: one poorly written and one well written. Both solutions are then scrutinized, and their affect on network performance is discussed.

Before discussing the two solutions, the next few sections discuss and clarify network related performance issues.

## Network Latency

Network bandwidth and network latency are separate terms. Networks with high bandwidth do not guarantee low latency. For example, a network path traversing a satellite link often has high latency, even though throughput is very high. It is not uncommon for a network round trip traversing a satellite link to have five or more seconds of latency. The implication of such a delay is this: an application designed to send a request, wait for a reply, send another request, wait for another reply, and so on, will wait at least five seconds for each packet exchange, regardless of how fast the server is. Despite the increasing speed of computers, satellite transmissions and network media are based on the speed of light, which generally stays constant. As such, improvements in latency for existing satellite networks is unlikely to occur.

## Network Saturation

Some saturation occurs in many networks. The easiest networks to saturate are slow modem links, such as standard 56k analog modems. However, Ethernet links with many computers on a single segment can also become saturated. The same is true about wide area networks with a low-bandwidth or otherwise overburdened link, such as a router or switch that can handle a limited amount of traffic. In such these cases, if the network sends more packets than its weakest link can handle, it drops packets. To avoid congestion the Windows TCP stack scales back when dropped packets are detected which can result in significant delays.

## Packet Processing Implications

When programs are developed for higher level environments like RPC, COM, and even Windows Sockets, developers tend to forget how much work takes place behind the scenes for each sent or received packet. When a packet arrives from the network, an interrupt from the network card is serviced by the computer. Then a Deferred Procedure Call (DPC) is queued, and must make its way through the drivers. If any form of security is used, the packet may have to be decrypted, or the cryptographic hash verified. A number of validity checks must also be performed at each state. Only then does the packet arrive at the final destination: the server code. Sending many small chunks of data results in packet processing overhead for each small chunk of data. Sending one big chunk of data tends to consume significantly less CPU time throughout the system, even though the cost of execution for many small chunks compared to one large chunk may be the same for the server application.

## Example 1: A Poorly Designed RPC Server

Imagine an application that must access remote files, and the task at hand is to design an RPC interface for manipulating the remote file. The simplest solution is to mirror the studio file routines for local files. Doing so may result in a deceptively clean and familiar interface. Here is an abbreviated .idl file:

``` syntax
typedef [context_handle] void *remote_file;
... .
interface remote_file
{
    remote_file remote_fopen(file_name);
    void remote_fclose(remote_file ...);
    size_t remote_fread(void *, size_t, size_t, remote_file ...);
    size_t remote_fwrite(const void *, size_t, size_t, remote_file ...);
    size_t remote_fseek(remote_file ..., long, int);
}
```

This seems elegant enough, but actually, this is a time-honored recipe for performance disaster. Contrary to popular opinion, remote procedure call is not simply a local procedure call with a wire between the caller and callee.

To see how this recipe burns performance, consider a 2K file, where 20 bytes are read from the beginning, and then 20 bytes from the end, and see how this performs. On the client side, the following calls are made (many code paths are omitted for brevity):

``` syntax
rfp = remote_fopen("c:\\sample.txt");
remote_read(...);
remote_fseek(...);
remote_read(...);
remote_fclose(rfp);
```

Now imagine that the server is separated from the client by a satellite link with a five-second round-trip time. Each of those calls must wait for a response before it can proceed, which means an absolute minimum for executing this sequence of 25 seconds. Considering we are retrieving only 40 bytes, this is outrageously slow performance. Customers of this application would be furious.

Now imagine the network is saturated, because a router's capacity somewhere in the network path is overburdened. This design forces the router to handle at least 10 packets if we do not have security (one for each request, and one for each reply). That, too, is not good.

This design also forces the server to receive five packets and send five packets. Again, not a very good implementation.

## Example 2: A Better Designed RPC Server

Let's redesign the interface discussed in Example 1, and see whether we can make it better. It is important to note that making this server really good requires knowledge of the usage pattern for the given files: such knowledge is not assumed for this example. Therefore, this is a better designed RPC server, but not an optimally designed RPC server.

The idea in this example is to collapse as many remote operations into one operation as possible. The first attempt is the following:

``` syntax
typedef [context_handle] void *remote_file;
typedef struct
{
    long position;
    int origin;
} remote_seek_instruction;
... .
interface remote_file
{
    remote_fread(file_name, void *, size_t, size_t, [in, out] remote_file ..., BOOL CloseWhenDone, remote_seek_instruction *...);
    size_t remote_fwrite(file_name, const void *, size_t, size_t, [in, out] remote_file ..., BOOL CloseWhenDone, remote_seek_instruction *...);
}
```

This example collapses all operations to a read and write, which allows for an optional open on the same operation, as well as an optional close and seek.

This same sequence of operation, when written in abbreviated form, looks like this:

``` syntax
remote_read("c:\\sample.txt", ..., &rfp, FALSE, NULL);
remote_read(NULL, ..., &rfp, TRUE, seek_to_20_bytes_before_end);
```

When considering the better designed RPC server, on the second call the server checks that the *file\_name* is **NULL**, and uses the stored open file in rfp. Then it sees there are seek instructions, and will position the file pointer 20 bytes before the end before it reads. When done, it will recognize the **CloseWhenDone** flag is set to **TRUE**, and will close the file, and close rfp.

On the high latency network, this better version takes 10 seconds to complete (2.5 times faster) and requires processing of only four packets; two receives from the server, and two sends from the server. The extra *ifs* and unmarshaling the server performs are negligible compared to everything else.

If causal ordering is specified properly, the interface can even be made asynchronous, and the two calls can be sent in parallel. When causal ordering is used calls are still dispatched in order, which means on the high latency network only a five-second delay is endured, even though the number of packets sent and received is the same.

We can collapse this even further by creating one method that takes an array of structures, each member of the array describing a particular file operation; a remote variation of scatter/gather I/O. The approach pays off as long as the result of each operation does not require further processing on the client; in other words the application is going to read the 20 bytes at the end regardless of what the first 20 bytes read are.

However, if some processing must be performed on the first 20 bytes after reading them to determine the next operation, collapsing everything into one operation does not work (at least not in all cases). The elegance of RPC is that an application can have both methods in the interface, and call either method depending on need.

In general, when the network is involved it is best to combine as many calls onto a single call as possible. If an application has two independent activities, use asynchronous operations and let them run in parallel. Essentially, keep the pipeline full.

 

 




