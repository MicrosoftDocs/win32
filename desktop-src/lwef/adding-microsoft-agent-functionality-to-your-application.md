---
title: Adding Microsoft Agent Functionality to Your Application
description: Adding Microsoft Agent Functionality to Your Application
ms.assetid: 2b4816dd-11bf-4c17-873e-4bdbb7fa1ccf
ms.topic: article
ms.date: 05/31/2018
---

# Adding Microsoft Agent Functionality to Your Application

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

To access Microsoft Agent's server interfaces, Agent must already be installed on the target system. Installation other than using Agent's self-installing executable file, such as attempting to copy and register Agent component files, is not supported. This ensures consistent and complete installation. Note that the Microsoft Agent self-installing file will not install on Microsoft Windows 2000 and later operating systems because these versions of the operating system already include their own version of Agent.

To successfully install Agent on a target system with a prior Microsoft Windows operating system, you must also ensure that the target system has a recent version of the Microsoft Visual C++ runtime (Msvcrt.dll), Microsoft registration tool (Regsvr32.dll), and Microsoft COM dlls. The easiest way to ensure that the necessary components are on the target system is to require that Microsoft Internet Explorer 3.02 or later is installed. Alternatively, you can install the first two components which are available as part of Microsoft Visual C++. The necessary COM dlls can be installed as part of the Microsoft DCOM update, available at the Microsoft website. You can find further information and licensing information for these components at the Microsoft website.

Agent's language components can be installed the same way. Similarly, you can use this technique to install the ACS format of the Microsoft characters available for distribution from the Microsoft Agent website. The character files automatically install to the Microsoft Agent \\Chars subdirectory.

Because Microsoft Agent's components are designed as operating system components, Agent may not be uninstalled. Similarly, where Agent is already installed as part of the Windows operating system, the Agent self-installing cabinet may not install.

Once installed, to call Agent's interfaces, create an instance of the server and request a pointer to a specific interface that the server supports using the standard COM convention. In particular, the COM library provides an API function, [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance), that creates an instance of the object and returns a pointer to the requested interface of the object. Request a pointer to the [**IAgent**](iagent.md) or [**IAgentEx**](iagentex.md) interface in your **CoCreateInstance** call or in a subsequent call to [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)).

The following code illustrates this in C/C++.


```
hRes = CoCreateInstance(CLSID_AgentServer,
                     NULL,
                     CLSCTX_SERVER,
                     IID_IAgentEx,
                     (LPVOID *)&amp;pAgentEx);
```



If the Microsoft Agent server is running, this function connects to the server; otherwise, it starts up the server.

Note that the Microsoft Agent server interfaces often include extended interfaces that include an "Ex" suffix. These interfaces are derived from, and therefore include all the functionality of, their non-Ex counterparts. If you want to use any of the extended features, use the Ex interfaces.

Functions that take pointers to BSTRs allocate memory using [**SysAllocString**](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-sysallocstring). It is the caller's responsibility to free this memory using [**SysFreeString**](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-sysfreestring).

 

 