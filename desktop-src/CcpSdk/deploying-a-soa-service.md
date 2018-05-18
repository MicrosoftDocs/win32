---
Description: 'Deploying a SOA-based service in a compute cluster requires deploying the service DLL and registering the service.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '12e8e094-b4e2-4133-a609-d49a060115d0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Deploying a SOA Service
---

# Deploying a SOA Service

Deploying a SOA-based service in a compute cluster requires deploying the service DLL and registering the service.

## Deploying the service DLL

The following table provides the options for deploying the service DLL. 

| Deployment option             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Local deployment<br/>   | Copy the service DLL to any folder on the root drive of each node in the cluster (for example, C:\\Services). This option yields the best performance, but updating the service binaries can be time-consuming in a large cluster, especially if all the nodes are not online at the same time.<br/>                                                                                                                                         |
| Central deployment<br/> | Copy the service DLL to a file share in the cluster. This option makes it easy to update the service binaries; however, it may result in longer DLL load times if the service binaries are large. You will also need to set up the .Net security permissions. For details on how to set up .Net security permissions, see the [Code Access Security Policy Tool](http://go.microsoft.com/fwlink/p/?linkid=122770) (Caspol.exe) in MSDN.<br/> |
| Hybrid deployment<br/>  | Copy large service binaries that are not updated often to the local nodes, while small or more frequently updated services are copied to a file share.<br/>                                                                                                                                                                                                                                                                                  |



 

## Registering the service DLL

You must register the service DLL with the compute cluster. Registering the service DLL requires a service registration file. The registration file is an XML file that specifies the path to the service DLL, the interface that defines the service contract and the class that implements the contract, and whether the service is of 32-bit or 64-bit binary. The file also specifies any environment variables that the service needs. You must name the configuration file *ServiceName***.config** (for example, EchoService.config).

The following example shows the contents of a service registration file. The only section that you need to modify is the **service** section.


```XML
<?xml version="1.0" encoding="utf-8" ?>
<configuration>

    <configSections>

        <!--Register service's custom configruation sections and group-->
        <sectionGroup name="microsoft.Hpc.Session.ServiceRegistration"
                      type="Microsoft.Hpc.Scheduler.Session.Configuration.ServiceRegistration, Microsoft.Hpc.Scheduler.Session, Version=2.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35">

            <section name="service"
                     type="Microsoft.Hpc.Scheduler.Session.Configuration.ServiceConfiguration, Microsoft.Hpc.Scheduler.Session, Version=2.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35"
                     allowDefinition="Everywhere"
                     allowExeDefinition="MachineToApplication"/>
          
        </sectionGroup>

    </configSections>

    <microsoft.Hpc.Session.ServiceRegistration>

        <service assembly="C:\Services\EchoService.dll"
                 contract="EchoService.IEchoService"
                 type="EchoService.EchoService"
                 architecture="AnyCpu">

            <!-- Environment variables used by the service -->
            <environmentVariables>
                <add name="myname1" value="myvalue1"/>
                <add name="myname2" value="myvalue2"/>
            </environmentVariables>

        </service>

    </microsoft.Hpc.Session.ServiceRegistration>

</configuration>

```



The following table provides a description of the **service** attributes.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Required</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>assembly</strong><br/></td>
<td>The full path to the service DLL.<br/> You can deploy the assemblies that the service DLL references but that are not installed in the global assembly cache (GAC) to one of the following locations:<br/>
<ul>
<li>The same path as the service DLL.<br/></li>
<li>Any folders in the PATH environment variable that you specified in the environmentVariables section of the <em>servicename</em>.config file.<br/></li>
</ul></td>
<td>Yes<br/></td>
</tr>
<tr class="even">
<td><strong>contract</strong><br/></td>
<td>The fully qualified name of the service's interface.<br/></td>
<td>Optional. If the DLL contains only one interface, this attribute is optional. However, for performance reasons you should always specify this attribute so that the session does not have to look up the name.<br/></td>
</tr>
<tr class="odd">
<td><strong>type</strong><br/></td>
<td>The fully qualified name of the class that implements the service's interface.<br/></td>
<td>Optional. Specify this attribute only if you specify the <strong>contract</strong> attribute.<br/></td>
</tr>
<tr class="even">
<td><strong>architecture</strong><br/></td>
<td>Specifies whether the service is a 32-bit or 64-bit binary. The possible values are &quot;AnyCpu&quot;, &quot;x86&quot;, and &quot;x64&quot;. Managed clients that do not invoke 32-bit or 64-bit calls should specify &quot;AnyCpu&quot;.<br/></td>
<td>Optional. The default is &quot;AnyCpu&quot;.<br/></td>
</tr>
</tbody>
</table>



 

You can register the service DLL locally on each node in the cluster or you can register it on a central share in the cluster. To register the DLL locally, place the completed registration file in the service registration folder located at %CCP\_HOME%\\ServiceRegistration.

To register the DLL on a central share in the cluster, set the cluster-wide environment variable CCP\_SERVICEREGISTRATION\_PATH to the location of the folder containing the registration file. To set the CCP\_SERVICEREGISTRATION\_PATH environment variable, use the cluster configuration (Cluscfg.exe) tool as shown in the following example. The share must be readable by everyone.

`cluscfg setenvs CCP_SERVICEREGISTRATION_PATH=\\<server>\<share>\`

Note that for each version of the service that you deploy, you must create a new service registration file.

## Testing the deployment

To determine if your service was successfully deployed in the cluster, you can use the SOA Service Configurations report. The following procedure shows how to run the report.

**To run the SOA Service Configurations report**

1.  Open the HPC Cluster Manager on the head node.
2.  Click **Diagnostics** in the Navigation pane.
3.  Under **Tests** in the tree view, click **SOA**.
4.  Select SOA Service Configurations Report from the list.
5.  Click the **Run** action.
6.  In the **Run Diagnostics** dialog, select the nodes to test.

The following procedure shows how to check test result after the SOA Service Configurations report completes.

**To check test results after the SOA Service Configurations report completes**

1.  In the **Diagnostics** tree view, click **Complete** under **Test Results**.
2.  Select SOA Service Configurations Report from the list.
3.  In the Result page, click a node to see if the service in installed on the node.

 

 




