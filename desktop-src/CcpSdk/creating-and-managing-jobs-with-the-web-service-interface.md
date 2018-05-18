---
Description: 'SP2), Microsoft HPC Pack provides access to the HPC Job Scheduler Service by using an HTTP web service that is based on the representational state transfer (REST) model.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '05C11C03-F9BB-47DB-AF6D-34582C1A486B'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Working with the Web Service Interface in Microsoft HPC Pack
---

# Working with the Web Service Interface in Microsoft HPC Pack

Beginning with Microsoft HPC Pack 2008 R2 with Service Pack 2 (SP2), Microsoft HPC Pack provides access to the HPC Job Scheduler Service by using an HTTP web service that is based on the representational state transfer (REST) model. You can use this REST API to create client applications that users can use to define, submit, modify, list, view, requeue, and cancel jobs.

Later versions of HPC Pack, including HPC Pack 2012, expand the HTTP web service to provide additional operations that provide information about nodes, to create and manage service-oriented architecture (SOA) sessions, and to send SOA requests and receive SOA responses for these sessions. The SOA operations are available only when the REST web service is hosted in Azure. All other operations are available either when the REST web service is hosted on an on-premises cluster or when the REST web service is hosted in Azure.

You can use the REST API in many programming languages to create client applications, including programming languages that the .NET and COM APIs for Microsoft HPC Pack do not support. You can also use to the REST API to create client applications that users on many operating systems can access, including operating systems that are not Windows-based.

## Installing and Configuring the REST API

The web service is included in the HPC Pack web features installation package.

**To install the HPC web features**

1.  In Windows Explorer on the head node of your HPC cluster, navigate to the Setup folder on the installation media for a supported version of Microsoft HPC Pack, or open the folder that you extracted from the file that you downloaded from the Microsoft Download Center.
2.  Double-click **HpcWebComponents.msi**.
3.  Follow the instructions in the **Microsoft HPC Pack Web Components Setup** wizard.

You can use the Set-HPCWebComponents.ps1 script to configure the REST API after you install the REST API. For example, you can use the script to change the port or the method to authenticate client credentials that the REST API uses. This script is located in the %CCP\_HOME%\\bin folder on the head node after you install the HPC web features.

The following example shows the syntax for the Set-HPCWebComponents.ps1 script.

``` syntax
Set-HPCWebComponent.ps1 -Service service_name -enable -Certificate thumbprint_value [-Port port_number] [-AuthenticationMethod method_name]
```

``` syntax
Set-HPCWebComponent.ps1 -Service service_name -disable 
```

The following table describes the parameters for the Set-HPCWebComponents.ps1 script. For detailed information to configure the web components, see [Installing the HPC Pack Web Components](https://TechNet.Microsoft.Com/library/hh314627.aspx).



| Parameter            | Description                                                                                                                                                                                                         |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Service              | Required. Specifies the name of the web component that you want to configure. Specify REST to configure the REST API, or specify Portal to specify the web portal page.<br/>                                  |
| enable               | Turns on the specified component.<br/>                                                                                                                                                                        |
| disable              | Turns off the specified component.<br/>                                                                                                                                                                       |
| Certificate          | Specifies the value of the Thumbprint property for the Secure Sockets Layer (SSL) certificate that you want to use to secure the web service.<br/>                                                            |
| Port                 | The port on which you want to open the service. The default port is 443.<br/>                                                                                                                                 |
| AuthenticationMethod | The authentication method that you want to use to authenticate the credentials that the client application provides. The possible values are Basic and NTLM. The default authentication method is Basic.<br/> |



 

The following example turns on the REST web service for port 8000 with NTLM authentication.


```PowerShell
Set-HPCWebComponents -Service REST -enable -Certificate 33CE10B55FE9A657815C3B19791340E375B7DF7C -AuthenticationMethod NTLM -Port 8000
```



The following example turns off the REST web service.


```PowerShell
Set-HPCWebComponents.ps1 -Service REST -disable
```



## Operations in the REST API

The HPC REST API defines a number of operations that you can perform, including the information that is expected in the HTTP requests that you send to the HPC REST web service and that is provided in the HTTP responses that you receive in return as part of each operation.

> [!Note]
>
> The HPC REST API does not define the manner in which you create and send these HTTP requests and process the HTTP responses. The approach you can use to work with the HTTP requests and responses varies depending on the programming language that you use, and can also vary depending on the libraries or other tools that you choose to install to work with HTTP requests and responses in your programming language of choice. Additional information about working with the HTTP requests and responses is beyond the scope of this documentation. For an example of how to work with HTTP requests and responses for operations in the HPC REST API, see [Creating and Submitting Jobs by Using the REST API in Microsoft HPC Pack](http://social.technet.microsoft.com/wiki/contents/articles/7737.creating-and-submitting-jobs-by-using-the-rest-api-in-windows-hpc-server-2008-r2.aspx).

 

For detailed information on the operations that are available in the HPC REST API both when the REST web service is hosted in an on-premises cluster, and when the REST web service is hosted in Azure, see [HPC Web Service API Reference](HttpS://MSDN.Microsoft.Com/library/hh560258.aspx).

## Getting Sample Programs that use the REST API

The SDK code samples for Microsoft HPC Pack include sample client applications that use the REST API. For information about the available versions of the Microsoft HPC Pack SDK and code samples, see [Microsoft High Performance Computing for Developers](HttpS://MSDN.Microsoft.Com/library/ff976568.aspx).

For example, the code samples for Microsoft HPC Pack 2008 R2 with SP2 include sample client applications in C# and Python that use the operations related to jobs and tasks. The code samples for later versions of Microsoft HPC Pack include updated versions of these C# and Python applications, and additional sample client applications in C and Java that use the SOA operations.

For Microsoft HPC Pack 2008 R2 with SP2, the C# example requires that you install the WCF REST Starter Kit Preview 2. For information about how to download the WCF REST Starter Kit Preview 2, see <http://aspnet.codeplex.com/releases/view/24644>.

For later versions of Microsoft HPC Pack, the C# example no longer requires that you install the WCF REST Starter Kit Preview 2. The C example requires the CURL and json-c libraries. For information about these libraries, see <http://curl.haxx.se> and <https://github.com/jehiah/json-c>.

 

 




