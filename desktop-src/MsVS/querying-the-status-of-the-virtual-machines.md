---
title: Querying the Status of the Virtual Machines
description: All of the virtual machine sessions controlled by Virtual Server are contained in a single top-level collection object.
ms.assetid: 'b84637e4-8b11-4df0-945d-98e2b12a336a'
---

# Querying the Status of the Virtual Machines

All of the virtual machine sessions controlled by Virtual Server are contained in a single top-level collection object. Querying the status of all the virtual machine sessions is accomplished by enumerating the collection object to obtain the interface pointers to each individual virtual machine session.

## Procedure for displaying virtual machine status

The general procedure for displaying the status of Virtual Server's virtual machine sessions is as follows:

1.  Initialize COM and obtain the interface pointer to the [**IVMVirtualServer**](ivmvirtualserver.md) object. See [Connecting to the Virtual Server COM Object](connecting-to-the-virtual-server-com-object.md).
2.  Obtain the individual [**IVMVirtualMachine**](ivmvirtualmachine.md) interface pointers to each virtual machine session by enumerating the [**IVMVirtualMachineCollection**](ivmvirtualmachinecollection.md) object contained in the [**IVMVirtualServer.VirtualMachines**](ivmvirtualserver-virtualmachines.md) property.
3.  Display the current virtual machine status by reading the [**VMVMState**](vmvmstate.md) value contained in the [**IVMVirtualMachine.State**](ivmvirtualmachine-state.md) property. The virtual machine session's computer name is contained in the [**IVMVirtualMachine.Name**](ivmvirtualmachine-name.md) property.
4.  Release all interface pointers and BSTR values returned by Virtual Server which are no longer being referenced.

## Displaying virtual machine status using Visual C++

The following console example program illustrates the steps required to enumerate and display the status of all virtual machine sessions running on Virtual Server. It uses the connection code from [Connecting to the Virtual Server COM Object](connecting-to-the-virtual-server-com-object.md) to initialize COM.

For clarity, error checking in this example program is rudimentary. All COM calls are checked for errors, and program execution will halt on any COM error after displaying the error code in hexadecimal.


```C++
// EnumVMs.cpp :
//  Console application to display the current status of all virtual 
//  machine sessions running under Virtual Server.
//
#define _WIN32_DCOM
#include "VSComInterfaces.h"
#include <atlbase.h>
#include <comdef.h>

// Routine to initialize COM and return an interface pointer to the
//   Virtual Server COM object.
extern HRESULT InitVSComInterfaces(_TCHAR* pRemoteServerName, 
                                   IVMVirtualServer** ppIVS);

// Routine to uninitialize COM.
extern HRESULT UninitVSComInterfaces(IVMVirtualServer* pIVS);

// MAIN PROGRAM
int _tmain(int argc, _TCHAR* argv[])
{
  _TCHAR* pRemoteServerName = NULL;
  HRESULT hr = S_OK;
  _bstr_t bAppName, bVersion;
  IVMVirtualServer* pIVS = NULL;
  IVMVirtualMachineCollection* pIVMColl = NULL;
  IVMVirtualMachine* pIVM = NULL;
  VMVMState vmState = vmVMState_Invalid;
  _TCHAR* pStateDesc[] = {"Invalid",
                          "Turned Off",
                          "Saved",
                          "Turning On",
                          "Restoring",
                          "Running",
                          "Paused",
                          "Saving",
                          "Turning Off",
                          "Merging Drives",
                          "Deleting Machine" };

  // Check for command line help flag
  if (--argc)
  {
    ++argv;
    // help switch?
    if (**argv == '-' || _tcscmp(*argv,"/?") == 0)
    {
      printf("USAGE: EnumVMs {remote_server_name}\n\n");
      printf("This utility displays the status of all the virtual machine sessions running\n");
      printf("on Virtual Server. If it is run without arguments then the local machine is\n");
      printf("accessed, otherwise the remote server specified will be accessed using DCOM.\n");
      exit(0);
    }
    pRemoteServerName = *argv;
  }

  // Initialize COM and output the Virtual Server version number to 
  // the console.
  if (FAILED(hr = InitVSComInterfaces(pRemoteServerName, &amp;pIVS)))
      goto ShowErr;
  if (FAILED(hr = pIVS->get_Name(bAppName.GetAddress())))
      goto ShowErr;
  if (FAILED(hr = pIVS->get_Version(bVersion.GetAddress())))
      goto ShowErr;

  printf("\n%ls version %ls\n", (wchar_t*)bAppName, 
                                (wchar_t*)bVersion);

  // Get the pointer to the virtual machine collection object.
  if (FAILED(hr = pIVS->get_VirtualMachines(&amp;pIVMColl)))
      goto ShowErr;

  // Check to see if there are any virtual machine sessions 
  // configured.
  long lCnt, lIdx;
  if (FAILED(hr = pIVMColl->get_Count(&amp;lCnt)))
      goto ShowErr;

  if (lCnt < 1)
  {
    printf(">> No virtual machines configured for this server\n");
    goto ExitIt;
  }

  // Start enumerating the virtual machine sessions
  for (lIdx = 1; lIdx <= lCnt; lIdx++)
  {
    _bstr_t bVMName;

    // Get the pointer to the virtual machine, then get the VM's 
    // session name and status
    if (FAILED(hr = pIVMColl->get_Item(lIdx, &amp;pIVM)))
        break;
    if (FAILED(hr = pIVM->get_Name(bVMName.GetAddress())))
        break;
    if (FAILED(hr = pIVM->get_State(&amp;vmState)))
        break;
  
    // Bounds check the status value so we can use it as an array 
    // index
    if (vmState < vmVMState_Invalid || vmState > vmVMState_DeleteMachine)
      vmState = vmVMState_Invalid;

    // Output the virtual machine name and status to the console.
    printf(">> %ls:%s\n", (wchar_t*)bVMName, pStateDesc[vmState]);
    pIVM->Release();
    pIVM = NULL;
  }

  // Skip error display if everything succeeded
  if (SUCCEEDED(hr)) goto ExitIt;

ShowErr:
  printf("ERROR: VSComInterfaces error %0lX\n",hr);

ExitIt:
  // Release any COM interface pointers that are still valid
  if (pIVM != NULL) pIVM->Release();
  if (pIVMColl != NULL) pIVMColl->Release();
  hr = UninitVSComInterfaces(pIVS);
}
```



 

 




