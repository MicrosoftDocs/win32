---
title: Using WinRM Windows PowerShell Cmdlets to Manage BITS Transfer Jobs
description: Windows Remote Management PowerShell cmdlets can manage Background Intelligent Transfer Service (BITS) transfer jobs.
ms.assetid: 9fbef8a1-ed3f-4277-9a07-ed427f60d7a8
ms.topic: article
ms.date: 05/31/2018
---

# Using WinRM Windows PowerShell Cmdlets to Manage BITS Transfer Jobs

Windows Remote Management PowerShell cmdlets can manage Background Intelligent Transfer Service (BITS) transfer jobs. For more information about BITS remote management, see [BITS provider](https://go.microsoft.com/fwlink/p/?linkid=154267) and [BITS provider classes]( https://go.microsoft.com/fwlink/p/?linkid=160847).

The following examples require the [BITS provider](https://go.microsoft.com/fwlink/p/?linkid=154267). The BITS provider is available after the BITS Compact server is installed. For information about installing the Compact server, see the [BITS Compact Server](bits-compact-server.md) documentation.

1.  Create a BITS transfer job.

    ```PowerShell
    # Get the credentials to connect to the remote client computer
    $cred = Get-Credential
    $result = Invoke-WsmanAction -Action CreateJob –Resourceuri wmi/root/microsoft/bits/BitsClientJob `
    –Valueset @{DisplayName="TestJob"; RemoteUrl="https://Server01/servertestdir/testfile1.txt"; LocalFile="C:\clienttestdir\testfile1.txt";Type=0} `
    –ComputerName Client1  -Credential $cred
    ```

    

    The [Get-Credential](https://go.microsoft.com/fwlink/p/?linkid=155904) cmdlet requests the user's credentials to connect to the remote computer and assigns the credentials to the $cred object.

    The [Invoke-WsmanAction](https://go.microsoft.com/fwlink/p/?linkid=155388) cmdlet creates the BITS transfer job on Client1 by creating an instance of the [BitsClientJob](https://go.microsoft.com/fwlink/p/?linkid=162152) class and using the information in the hash table defined in the *Valueset* parameter. The *Valueset* parameter specifies the information needed to populate the parameters of the [CreateJob](https://go.microsoft.com/fwlink/p/?linkid=162151) method. In the preceding example, the user is sets the *Type* parameter to 0 (download). The user also specifies the name of both the remote and local files for the download job. For more information about creating BITS transfer jobs and for detailed information about parameters, see [CreateJob](https://go.microsoft.com/fwlink/p/?linkid=162151) method.

    The [Invoke-WsmanAction](https://go.microsoft.com/fwlink/p/?linkid=155388) cmdlet assigns the result to the $result variable.

    > [!Note]  
    > The grave-accent character (\`) is used to indicate a line break.

     

2.  Set the Priority of the BITS transfer job.

    ```PowerShell
    Set-WsmanInstance  -ResourceURI  wmi/root/microsoft/bits/BitsClientJob -SelectorSet @{JobId=$result.JobId} `
    -ValueSet @{Priority=0} –ComputerName Client1  -Credential $cred
    ```

    

    The [Set-WsmanInstance](https://go.microsoft.com/fwlink/p/?linkid=155390) cmdlet changes the new BITS transfer job priority to 0 (**BG\_JOB\_PRIORITY\_FOREGROUND**). For more information about the priority levels, see the [**BG\_JOB\_PRIORITY**](/windows/desktop/api/Bits/ne-bits-__midl_ibackgroundcopyjob_0001) enumeration.

3.  Resume the BITS transfer job.

    ```PowerShell
    Invoke-WsmanAction -Action SetJobState -ResourceUri wmi/root/microsoft/bits/BitsClientJob  -selectorset @{JobId=$result.JobId}  `
    -valueset @{JobState= 2} –ComputerName Client1  -Credential $cred
    ```

    

    The [Invoke-WsmanAction](https://go.microsoft.com/fwlink/p/?linkid=155388) cmdlet calls the [SetJobState](https://go.microsoft.com/fwlink/p/?linkid=162153) method, which sets the job state to 2 (Resume the Job).

4.  Manage the BITS transfer job.

    ```PowerShell
    $IsPprocessing = $TRUE
    while ($IsPprocessing)
    {
        $result = Get-WsmanInstance  -ResourceURI  wmi/root/microsoft/bits/BitsClientJob -selectorset @{JobId = $result.JobId} `
               –ComputerName Client1  -Credential $cred
        if ($result.State -eq 6)
        {

    #Complete the job           
            Invoke-WsmanAction -action SetJobState -resourceuri wmi/root/microsoft/bits/BitsClientJob  -selectorset @{JobId=$result.JobId}  `
                          -valueset @{JobState= 1} –ComputerName Client1  -Credential $cred
            "Job Successfully Transferred"
            $IsPprocessing = $FALSE;
        }
        elseif (($result.State -eq 4) -or ($result.State -eq 5))
        {

    #Cancel the job
            "Job is in Error " 
            Invoke-WsmanAction -action SetJobState -resourceuri wmi/root/microsoft/bits/BitsClientJob  -selectorset @{JobId=$result.JobId}  `
                         -valueset @{JobState= 0} –ComputerName Client1  -Credential $cred
            # You can troubleshoot or delete the job
            $IsPprocessing = $FALSE;
        }
        else
        {
        "Job is processing\n" 
        }

    # Perform other action or poll in a tight loop. This example sleeps for 5 seconds
    sleep 5
    }
    ```

    

    The preceding example is a script to poll the status of the job and take an action based on the status. The following actions are possible:

    -   If $result.State is 4 (**BG\_JOB\_STATE\_ERROR**), the [Invoke-WsmanAction](https://go.microsoft.com/fwlink/p/?linkid=155388) cmdlet calls the [SetJobState](https://go.microsoft.com/fwlink/p/?linkid=162153) method and cancels the job.
    -   If $result.State is 5 (**BG\_JOB\_STATE\_TRANSIENT\_ERROR**), the [Invoke-WsmanAction](https://go.microsoft.com/fwlink/p/?linkid=155388) cmdlet calls the [SetJobState](https://go.microsoft.com/fwlink/p/?linkid=162153) method and cancels the job.
    -   If $result.State is 6 (**BG\_JOB\_STATE\_TRANSFERRED**), the [Invoke-WsmanAction](https://go.microsoft.com/fwlink/p/?linkid=155388) cmdlet calls the [SetJobState](https://go.microsoft.com/fwlink/p/?linkid=162153) method and sets the state to complete.

    For more information about job states, see the [**BG\_JOB\_STATE**](/windows/desktop/api/Bits/ne-bits-__midl_ibackgroundcopyjob_0002) enumeration.

## Related topics

<dl> <dt>

[Get-Credential](https://go.microsoft.com/fwlink/p/?linkid=155904)
</dt> <dt>

[Invoke-WsmanAction](https://go.microsoft.com/fwlink/p/?linkid=155388)
</dt> <dt>

[Set-WsmanInstance](https://go.microsoft.com/fwlink/p/?linkid=155390)
</dt> </dl>

 

 




