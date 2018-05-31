---
title: Connecting to the Virtual Server COM Object
description: The Virtual Server programming interface is a standard COM object.
ms.assetid: 1f9d5911-99ca-4ed0-a56e-cdfb322b53dd
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to the Virtual Server COM Object

The Virtual Server programming interface is a standard COM object. Before any of the interfaces are accessed, the COM layer is initialized, the default security access level is set, and a pointer to the main [**IVMVirtualServer**](ivmvirtualserver.md) object is obtained. All other Virtual Server objects are accessed through this primary interface.

The Virtual Server COM interfaces can only be accessed if the COM Security level is set to **Impersonation** level or higher. By default, COM uses the **Identification** security level if no level is explicitly specified. To set the COM security level, the user's program should make a call to [CoInitializeSecurity](Http://go.microsoft.com/fwlink/p/?linkid=84387) immediately after the initial [CoInitializeEx](Http://go.microsoft.com/fwlink/p/?linkid=84388) call and before any of the Virtual Server's interfaces are accessed.

The multithreaded apartment model should be used for applications using the Virtual Server COM interfaces. Using the single-threaded apartment model with the Virtual Server COM interface can significantly affect the Virtual Server system's performance.

The various Event interfaces are used by Virtual Server to communicate asynchronous status and state change information back to the application program. If the client application is run remotely, the DCOM service must be properly configured to work through any firewalls and routers which exist between the server and the client program. A white paper titled "Using Distributed COM with Firewalls" by Michael Nelson can be found in the Microsoft COM website in the white papers section. This article details the steps required to configure DCOM to work through firewalls.

## Accessing Virtual Server using Visual C#

Visual C# and .NET normally handles all the initialization and marshaling of the COM interface layer. To change the COM security level, the [CoInitializeSecurity](Http://go.microsoft.com/fwlink/p/?linkid=84387) must be called directly at the very beginning of the program, before any type of COM marshaling has been performed.

The following example program illustrates the steps required to initialize and access the Virtual Server COM object. It displays the name and version number of the Virtual Server COM object.

The following steps must be performed to set up the build environment:

1.  Create a new **Windows Applications** project called **ShowVSVersion**. **Form1** is created by default.
2.  Add a class to the project. **Class1** is created by default.
3.  Add the reference to the **Virtual Server 2005 Type Library**
4.  From the **Project** menu, choose **Properties** and define **ShowVSVersion.Class1**as the start-up procedure.
5.  Enter the following sample code into **Class1**:


```CSharp
using System;
using System.Reflection;
using System.Runtime.InteropServices;
using Microsoft.VirtualServer.Interop;

namespace ShowVSVersion
{
    /// <summary>
    /// Define RPC_C_AUTHN_LEVEL_ constants
    /// </summary>
    public enum RpcAuthnLevel
    {
        Default = 0,
        None,
        Connect,
        Call,
        Pkt,
        PktIntegrity,
        PktPrivacy
    }

    /// <summary>
    /// Define RPC_C_IMP_LEVEL_ constants
    /// </summary>
    public enum RpcImpLevel
    {
        Default = 0,
        Anonymous,
        Identify,
        Impersonate,
        Delegate
    }

    /// <summary>
    /// Define EOAC_ constants
    /// </summary>
    public enum EoAuthnCap
    {
        None =           0x0000,
        MutualAuth =     0x0001,
        StaticCloaking=  0x0020,
        DynamicCloaking= 0x0040,
        AnyAuthority=    0x0080,
        MakeFullSIC=     0x0100,
        Default=         0x0800,
        SecureRefs=      0x0002,
        AccessControl=   0x0004,
        AppID=           0x0008,
        Dynamic=         0x0010,
        RequireFullSIC=  0x0200,
        AutoImpersonate= 0x0400,
        NoCustomMarshal= 0x2000,
        DisableAAA=      0x1000
    }

    /// <summary>
    /// InitVS handles the special COM/DCOM startup code required by
    /// the Virtual Server security model.
    /// </summary>
    public class InitVS
    {
        // Create the call with PreserveSig:=FALSE so the COM InterOp
        // layer will perform the error checking and throw an 
        // exception instead of returning an HRESULT.
        //
        [ DllImport( "Ole32.dll",
                ExactSpelling=true,
                EntryPoint="CoInitializeSecurity",
                CallingConvention=CallingConvention.StdCall,
                SetLastError=false,
                PreserveSig=false) ]

        private static extern void CoInitializeSecurity(
            IntPtr pVoid,
            int    cAuthSvc,
            IntPtr asAuthSvc,
            IntPtr pReserved1,
            uint   dwAuthnLevel,
            uint   dwImpLevel,
            IntPtr pAuthList,
            uint   dwCapabilities,
            IntPtr pReserved3 );
      
        /// <summary>
        /// Call CoInitializeSecurity with dwImpLevel set to 
        /// Impersonate. Required by the Virtual Server COM Interface.  
        /// </summary>
        public InitVS()
        {
            CoInitializeSecurity(IntPtr.Zero, 
                -1, 
                IntPtr.Zero, 
                IntPtr.Zero,
                (uint)RpcAuthnLevel.PktPrivacy,
                (uint)RpcImpLevel.Impersonate,
                IntPtr.Zero,  
                (uint)EoAuthnCap.DynamicCloaking, 
                IntPtr.Zero );
        }

        /// <summary>
        /// Get VMVirtualServerClass instance from a remote server using DCOM
        /// </summary>
        /// <param name="server">Remote server name</param>
        /// <returns>Remote Virtual Server object class with DCOM enabled</returns>
        public VMVirtualServerClass GetVMVirtualServerClass(string server)
        {

            VMVirtualServerClass GetVMVirtualServerClass_result;
            Type                 typeVSClass;
            Type                 typeDCOM;
            object               objDCOM;

            typeVSClass = typeof(VMVirtualServerClass);
            typeDCOM = Type.GetTypeFromCLSID(typeVSClass.GUID, 
                                             server, 
                                             true);
            objDCOM = Activator.CreateInstance(typeDCOM);

            GetVMVirtualServerClass_result = 
                (VMVirtualServerClass) Marshal.CreateWrapperOfType(objDCOM, typeVSClass);
            return GetVMVirtualServerClass_result;
        }

        /// <summary>
        /// Get VMVirtualServerClass instance from local server using COM
        /// </summary>
        /// <returns>Local Virtual Server object class with COM enabled</returns>
        public VMVirtualServerClass GetVMVirtualServerClass()
        {
            VMVirtualServerClass GetVMVirtualServerClass_result;
            GetVMVirtualServerClass_result = 
                new VMVirtualServerClass();
            return GetVMVirtualServerClass_result;
        }
    }

    /// <summary>
    /// This class wraps the MsgBox function from user32.dll
    /// </summary>
    public class MyLib 
    {
        // Declares managed prototypes for unmanaged functions.
        [ DllImport( "User32.dll", 
                     EntryPoint="MessageBox", 
                     CharSet=CharSet.Auto )]

        public static extern int MsgBox( int    hWnd, 
                                         String text, 
                                         String caption, 
                                         uint   type );
    }

    /// <summary>
    /// Main program module
    /// </summary>
    class Class1
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [MTAThread]
        static void Main(string[] CmdArgs)
        {
            // Initialize COM with Impersonate first
            InitVS myApp;
            myApp = new InitVS();

            // Check command line arguments help flag
            if (CmdArgs.Length>0)
            {
                if (CmdArgs[0].Length > 1 &amp;&amp; 
                    (CmdArgs[0].Substring(0,1)=="-" || CmdArgs[0].Substring(0,2)=="/?"))
                {
                    String strHelp = "USAGE: ShowVSVersion {remote_server_name}\n\n";
                    strHelp += "This utility checks access to the Virtual Server COM object interface. If it\n";
                    strHelp += "is run without arguments then the local machine is accessed, otherwise the\n";
                    strHelp += "remote server specified will be accessed using DCOM.";

                    MyLib.MsgBox( 0, strHelp, "ShowVSVersion", 0);
                    return;
                }
            }

            // Connect locally or remotely
            VMVirtualServer myVS;
            try 
            {
                if (CmdArgs.Length>0)
                    myVS = myApp.GetVMVirtualServerClass(CmdArgs[0]);
                else
                    myVS = myApp.GetVMVirtualServerClass();
            }
            catch
            {
                MyLib.MsgBox(0, 
                             "Cannot connect to Virtual Server", 
                             "ShowVSVersion", 
                             0);
                return;
            }

            // Get Virtual Server name and version number
            string sName;
            string sVersion;

            sName = myVS.Name;
            sVersion = myVS.Version;

            MyLib.MsgBox(0, 
                         sName + " version " + sVersion, 
                         "ShowVSVersion", 
                         0);
        }
    }

}
```



## Accessing Virtual Server using Visual C++

Programs using the Virtual Server COM interface should initialize COM using the **Multi-Threaded** model. This requires that a call to [CoInitializeEx](Http://go.microsoft.com/fwlink/p/?linkid=84388) be used instead of [CoInitialize](Http://go.microsoft.com/fwlink/p/?linkid=84386). Using the **Apartment-Threaded** model with the Virtual Server interface can significantly affect the Virtual Server system's performance.

Setting the COM Security level to **Impersonation** level is accomplished by calling [CoInitializeSecurity](Http://go.microsoft.com/fwlink/p/?linkid=84387) immediately after the initial [CoInitializeEx](Http://go.microsoft.com/fwlink/p/?linkid=84388) call and before any of the Virtual Server's interfaces or other COM objects are accessed.

The following console example program illustrates the steps required to initialize and access the Virtual Server COM object.


```C++
// TestCOMLink.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


// TestCOMLink.cpp 
//   Console Application to test access to Virtual Server's COM 
//   programming interface.
//
// COM INITIALIZATION routine
//
HRESULT InitVSComInterfaces(_TCHAR* pRemoteServerName, 
                            IVMVirtualServer** ppIVS)
{
  // Check for required arguments
  if (ppIVS == NULL)
    return E_INVALIDARG;

  // Initialize COM to Free-Threaded. 
  //   (Virtual Server performance can be significantly 
  //    impacted if Apartment-Threaded is used.)
  *ppIVS = NULL;
  HRESULT hr = CoInitializeEx(NULL,COINIT_MULTITHREADED);
  if (FAILED(hr)) return hr;

  // Set default security level to IMPERSONATE. This is required by
  // the Virtual Server COM object's security model.
  hr = CoInitializeSecurity(NULL, 
                            -1, 
                            NULL, 
                            NULL, 
                            RPC_C_AUTHN_LEVEL_PKT_PRIVACY,
                            RPC_C_IMP_LEVEL_IMPERSONATE,
                            NULL, EOAC_DYNAMIC_CLOAKING, 
                            NULL);
  if (FAILED(hr)) return hr;
  
  REFCLSID classID = _uuidof(VMVirtualServer);

  // Running on the same machine as Virtual Server?
  if (pRemoteServerName == NULL)
    hr = CoCreateInstance(classID, 
                          NULL, 
                          CLSCTX_ALL, 
                          IID_IVMVirtualServer, 
                          (LPVOID*)ppIVS);

  // Not local. Running on a remote machine?
  else
  {
    // Yes, connect remotely via DCOM
    CComBSTR    serverName(pRemoteServerName);
    MULTI_QI    multiQI = { &amp;IID_IVMVirtualServer, NULL, NOERROR };
    COSERVERINFO  serverInfo = { 0, serverName, NULL, 0 };
    hr = CoCreateInstanceEx(classID, 
                            NULL, 
                            CLSCTX_ALL, 
                            &amp;serverInfo, 
                            1, 
                            &amp;multiQI);

    // get interface pointer
    if (SUCCEEDED(hr))
      *ppIVS = (IVMVirtualServer*)(multiQI.pItf);
  }

  // test connection
  if (SUCCEEDED(hr) &amp;&amp; (*ppIVS != NULL))
  {
    // Make a call to the interface and see if it works.
    _bstr_t bVer;
    hr = (*ppIVS)->get_Version(bVer.GetAddress());
  }
  return hr;
}

// COM UNINITIALIZATION routine
HRESULT UninitVSComInterfaces(IVMVirtualServer* pIVS)
{
  HRESULT hr = S_OK;
  if (pIVS != NULL)
  {
    hr = pIVS->Release();
    pIVS = NULL;
  }
  CoUninitialize();
  return hr;
}

// MAIN PROGRAM
int _tmain(int argc, _TCHAR* argv[])
{
  _TCHAR* pRemoteServerName = NULL;
  HRESULT hr = S_OK;
  IVMVirtualServer* pIVS = NULL;

  // Check for help flag and print help
  if (--argc)
  {
    ++argv;
    // help switch?
    if (**argv == TEXT('-') || _tcscmp(*argv,TEXT("/?")) == 0)
    {
      _tprintf(TEXT("USAGE: TestCOMLink {remote_server_name}\n\n"));
      _tprintf(TEXT("This utility checks access to the Virtual Server COM object interface. If it\n"));
      _tprintf(TEXT("is run without arguments then the local machine is accessed, otherwise the\n"));
      _tprintf(TEXT("remote server specified will be accessed using DCOM.\n"));
      exit(0);
    }
    pRemoteServerName = *argv;
  }

  // Initialize the COM layer
  hr = InitVSComInterfaces(pRemoteServerName, &amp;pIVS);
  if (FAILED(hr))
    _tprintf(TEXT("Init error: %0lX\n"), hr);
  else
  {
    // Display name and version number
    _bstr_t bAppName, bVersion;
    hr = pIVS->get_Name(bAppName.GetAddress());
    if (SUCCEEDED(hr))
      hr = pIVS->get_Version(bVersion.GetAddress());
    if (FAILED(hr))
      _tprintf(TEXT("VSComInterfaces initialized, error %0lX when retrieving version info\n"), hr);
    else
      _tprintf(TEXT("\n%ls version %ls\n"), (wchar_t*)bAppName, (wchar_t*)bVersion);
  }

  // Exit gracefully
  hr = UninitVSComInterfaces(pIVS);
}
```



The initialization and uninitialization routines in the preceding example can easily be wrapped into a class constructor and destructor if the user's program is based on an application object.

 

 




