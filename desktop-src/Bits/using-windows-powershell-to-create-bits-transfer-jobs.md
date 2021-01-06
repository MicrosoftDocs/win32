---
title: Using Windows PowerShell to Create BITS Transfer Jobs
description: You can use PowerShell cmdlets to create synchronous and asynchronous Background Intelligent Transfer Service (BITS) transfer jobs.
ms.assetid: 22bcf0d5-36f0-4677-84a7-502b98cfaac2
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Using Windows PowerShell to Create BITS Transfer Jobs

You can use PowerShell cmdlets to create synchronous and asynchronous Background Intelligent Transfer Service (BITS) transfer jobs.

All of the examples in this topic use the [Start-BitsTransfer](/previous-versions//dd347701(v=technet.10)) cmdlet. To use the cmdlet, be sure to import the module first. To install the module, run the following command: Import-Module BitsTransfer. For more information, type **Get-Help Start-BitsTransfer** at the PowerShell prompt.

> [!IMPORTANT]
>
> When you use [\*-BitsTransfer](/previous-versions//dd819413(v=technet.10)) cmdlets from within a process that runs in a noninteractive context, such as a Windows service, you may not be able to add files to BITS jobs, which can result in a suspended state. For the job to proceed, the identity that was used to create a transfer job must be logged on. For example, when creating a BITS job in a PowerShell script that was executed as a Task Scheduler job, the BITS transfer will never complete unless the Task Scheduler's task setting "Run only when user is logged on" is enabled.

 

-   [To create a synchronous BITS transfer job](#to-create-a-synchronous-bits-transfer-job)
-   [To create a synchronous BITS transfer job with multiple files](#to-create-a-synchronous-bits-transfer-job-with-multiple-files)
-   [To create a synchronous BITS transfer job and specify credentials for a remote server](#to-create-a-synchronous-bits-transfer-job-and-specify-credentials-for-a-remote-server)
-   [To create a synchronous BITS transfer job from a CSV file](#to-create-a-synchronous-bits-transfer-job-from-a-csv-file)
-   [To create an asynchronous BITS transfer job](#to-create-an-asynchronous-bits-transfer-job)
-   [To manage PowerShell Remote sessions](#to-manage-powershell-remote-sessions)
-   [Related topics](#related-topics)

## To create a synchronous BITS transfer job


```PowerShell
Start-BitsTransfer -Source https://Server01/serverdir/testfile1.txt `
-Destination C:\clientdir\testfile1.txt
```



> [!Note]  
> The grave-accent character (\`) is used to indicate a line break.

 

In the preceding example, the local and remote names of the file are specified in the *Source* and *Destination* parameters, respectively. The command prompt returns when the file transfer is complete or when it enters an error state.

The default transfer type is Download. When you upload files to an HTTP location, the *TransferType* parameter must be set to Upload.

Because parameter position is enforced for the [Start-BitsTransfer](/previous-versions//dd347701(v=technet.10)) cmdlet, the parameter names do not need to be specified for the Source and Destination parameters. Therefore, this command can be simplified as follows.


```PowerShell
Start-BitsTransfer https://Server01/serverdir/testfile1.txt C:\clientdir\testfile1.txt
```



## To create a synchronous BITS transfer job with multiple files


```PowerShell
Start-BitsTransfer -Source C:\clientsourcedir\*.txt `
-Destination c:\clientdir\ -TransferType Download
```



In the preceding example, the [Start-BitsTransfer](/previous-versions//dd347701(v=technet.10)) command creates a new BITS transfer job. All of the files are added to this job and transferred sequentially to the client.

> [!Note]  
> The destination path cannot use wildcard characters. The destination path supports relative directories, root paths, or implicit directories (that is, the current directory). Destination files cannot be renamed by using a wildcard character. Additionally, HTTP and HTTPS URLs do not work with wildcards. Wildcards are only valid for UNC paths and local directories.

 

## To create a synchronous BITS transfer job and specify credentials for a remote server


```PowerShell
Start-BitsTransfer -DisplayName MyJob -Credential Username\Domain `
-Source https://server01/servertestdir/testfile1.txt -Destination c:\clienttestdir\testfile1.txt `
-ProxyUsage Override -ProxyList @(https://proxy1, 123.24.21.23, proxy3)
```



In the preceding example, a user creates a BITS transfer job to download a file from a server that requires authentication. The user is prompted for credentials, and the *Credential* parameter passes a credential object to the [Start-BitsTransfer](/previous-versions//dd347701(v=technet.10)) cmdlet. The user sets an explicit proxy, and the BITS transfer job uses only the proxies that are defined by the *ProxyList* parameter. The *DisplayName* parameter gives the BITS transfer job a unique display name.

## To create a synchronous BITS transfer job from a CSV file


```PowerShell
Import-CSV filelist.txt | Start-BitsTransfer -TransferType Upload
```



> [!Note]  
> The "\|" is the pipe character.

 

In the preceding example, a user creates a BITS transfer job that uploads multiple files from a client. The [Import-CSV](/previous-versions//dd347665(v=technet.10)) cmdlet imports the source and destination file locations and pipes them to the [Start-BitsTransfer](/previous-versions//dd347701(v=technet.10)) command. The [Start-BitsTransfer](/previous-versions//dd347701(v=technet.10)) command creates a new BITS transfer job for each file, adds the files to the job, and then transfers them sequentially to the server.

The contents of the Filelist.txt file should be in the following format:

``` syntax
Source, Destination
c:\clienttestdir\testfile1.txt, https://server01/servertestdir/testfile1.txt
c:\clienttestdir\testfile2.txt, https://server01/servertestdir/testfile2.txt
c:\clienttestdir\testfile3.txt, https://server01/servertestdir/testfile3.txt
c:\clienttestdir\testfile4.txt, https://server01/servertestdir/testfile4.txt
```

## To create an asynchronous BITS transfer job


```PowerShell
$Job = Start-BitsTransfer -Source https://Server1.TrustedDomain.com/File1.zip `
       -Destination d:\temp\downloads\ -Asynchronous

while (($Job.JobState -eq "Transferring") -or ($Job.JobState -eq "Connecting")) `
       { sleep 5;} # Poll for status, sleep for 5 seconds, or perform an action.

Switch($Job.JobState)
{
    "Transferred" {Complete-BitsTransfer -BitsJob $Job}
    "Error" {$Job | Format-List } # List the errors.
    default {"Other action"} #  Perform corrective action.
}

```



In the preceding example, the BITS transfer job was assigned to the $Job variable. The files are downloaded sequentially. After the transfer job is complete, the files are immediately available. If $Job.JobState returns "Transferred", the $Job object is sent to the [Complete-BitsTransfer]( /previous-versions//dd347701(v=technet.10)) cmdlet.

If $Job.JobState returns "Error", the $Job object is sent to the [Format-List]( /previous-versions//dd347700(v=technet.10)) cmdlet to list the errors.

## To manage PowerShell Remote sessions

Starting with Windows 10, version 1607, you can run PowerShell Cmdlets, BITSAdmin, or other applications that use the BITS [interfaces](bits-interfaces.md) from a PowerShell Remote command line connected to another machine (physical or virtual). This capability is not available when using a [PowerShell Direct](/virtualization/hyper-v-on-windows/user_guide/vmsession) command line to a virtual machine on the same physical machine, and it is not available when using WinRM cmdlets.

A BITS Job created from a Remote PowerShell session runs under that session’s user account context and will only make progress when there is at least one active local logon session or Remote PowerShell session associated with that user account. You can use PowerShell's persistent PSSessions to run remote commands without the need to keep a PowerShell window open for each job to continue making progress, as described in [PowerShell Basics: Remote Management](https://techgenix.com/remote-management-powershell-part1/).

-   [New-PSSession](/powershell/module/microsoft.powershell.core/new-pssession?view=powershell-7&preserve-view=true) creates a persistent Remote PowerShell session. Once created, the PSSession objects persist in the remote machine until explicitly deleted. Any BITS jobs initiated in an active session will make progress transferring data, even after the client has disconnected from the session.
-   [Disconnect-PSSession](/powershell/module/microsoft.powershell.core/disconnect-pssession?view=powershell-7&preserve-view=true) disconnects the client machine from a Remote PowerShell session and the session’s state continues to be maintained by the remote machine. Most importantly, the remote session’s processes will continue executing, and BITS jobs will continue to make progress. The client machine can even reboot and/or turn off after calling Disconnect-PSSession.
-   [Connect-PSSession](/powershell/module/microsoft.powershell.core/connect-pssession?view=powershell-7&preserve-view=true) re-connects the client machine to an active Remote PowerShell session.
-   [Remove-PSSession](/powershell/module/microsoft.powershell.core/remove-pssession?view=powershell-7&preserve-view=true) tears down a Remote PowerShell session.

The example below shows how to use PowerShell Remote to work with asynchronous BITS transfer jobs in a way that allows the job to continue to make progress even when you are not actively connected to the remote session.


```PowerShell
# Establish a PowerShell Remote session in Server01 with name 'MyRemoteSession'
New-PSSession -ComputerName Server01 -Name MyRemoteSession -Credential Domain01\User01

# Enter the previously-established session to execute commands
Enter-PSSession -Name MyRemoteSession

# Enumerate active BITS transfers on the remote machine
Get-BitsTransfer

# While running in the context of the PowerShell Remote session, start a new BITS transfer
Start-BitsTransfer -Source https://Server1.TrustedDomain.com/File1.zip -Destination c:\temp\downloads\ -Asynchronous

# Exit the PowerShell Remote session's context
Exit-PSSession

# Disconnect the 'MyRemoteSession' PowerShell Remote session from the current PowerShell window
# After this command, it is safe to close the current PowerShell window and turn off the local machine
Disconnect-PSSession -Name MyRemoteSession


# The commands below can be executed from a different PowerShell window, even after rebooting the local machine
# Connect the 'MyRemoteSession' PowerShell Remote session to the current PowerShell window
Connect-PSSession -ComputerName Server01 -Name MyRemoteSession

# Enter the previously-established session to execute commands
Enter-PSSession -Name MyRemoteSession

# Enumerate active BITS transfers on the remote machine
Get-BitsTransfer

# Manage BITS transfers on the remote machine via Complete-BitsTransfer, Remove-BitsTransfer, etc.

# Exit the PowerShell Remote session's context
Exit-PSSession

# Destroy the 'MyRemoteSession' PowerShell Remote session when no longer needed
Remove-PSSession -Name MyRemoteSession
```



## Related topics

<dl> <dt>

[Start-BitsTransfer](/previous-versions//dd347701(v=technet.10))
</dt> <dt>

[Complete-BitsTransfer]( /previous-versions//dd347701(v=technet.10))
</dt> </dl>

 

 
