---
Description: 'To use HPC sessions, you need to configure one or more nodes in the cluster to run broker jobs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1048c1bc-e5ea-4252-8a2f-478c8bebc6e4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Configuring Nodes to Run HPC Sessions
---

# Configuring Nodes to Run HPC Sessions

To use HPC sessions, you need to configure one or more nodes in the cluster to run broker jobs. The following procedure shows how to configure a node to run broker jobs.

**To configure a node to run broker jobs**

1.  Open the HPC Cluster Manager on the head node.
2.  Click **Node Management** in the Navigation pane.
3.  The node must be offline in order to change its role.
4.  In the tree view, click **Offline** under **By State**.
5.  In the list of offline nodes, right-click the node that you want to designate as a broker node.
6.  Click **Change Role** in the context menu.
7.  Select the **WCF broker node** option in the **Change Node Role** dialog box.

If the designation is successful, the node will be listed in the WCFBrokerNodes node group (in the **Node Management** tree view click **WCFBrokerNodes** under **By Group**).

For a node to become a broker node, it must have direct enterprise network connectivity. Typically, you want to select a node with many cores and a large amount of memory so that it can support larger message sizes and a higher throughput of messages (more messages).

You can designate more than one node to become a broker node. To determine how many nodes to designate as a broker node, use the following formula.

Max (n \* r / throughput-per-box, n \* l \* s / memory-per-box)

where <dl> *n* is the average (or peek) number of sessions to host  
*r* is the average rate of messages per session  
*n \* r* is the number of messages to process  
*l* is the input queue length (see [BrokerSettingsInfo.MessagesThrottleStartThreshold](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.brokersettingsinfo.messagesthrottlestartthreshold.aspx))  
*s* is the average size of a message  
*l \* s* is the memory usage per broker  
</dl>

The first parameter of the Max function determines the number of nodes that you need to support the required throughput, and the second parameter determines the number of nodes that you need to support the average message size. Choose the larger number of nodes.

Note that configuring a node to run broker jobs prevents it from running other types of jobs.

## SOA Model Latency

The SOA Model Latency report checks the system configuration and run-time performance of the SOA infrastructure so that you can ensure that the system is ready to run SOA workloads and can determine whether the system has any bottlenecks. The following procedure shows how to run the SOA Model Latency report.

**To run the SOA Model Latency report**

1.  Open the HPC Cluster Manager on the head node.
2.  Click **Diagnostics** in the Navigation pane.
3.  Under **Tests** in the tree view, click **SOA**.
4.  Select SOA Model Latency from the list.
5.  Click the **Run** action.
6.  In the **Run Diagnostics** dialog, select the nodes to test.

The following procedure shows how to check test results after the SOA Model Latency report completes.

**To check test results after the SOA Model Latency report completes**

1.  In the **Diagnostics** tree view, click **Complete** under **Test Results**.
2.  Select SOA Model Latency from the list.
3.  In the Result page, click the different report features for results.

 

 



