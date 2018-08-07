---
title: BITSAdmin Tool
description: BITSAdmin is a command-line tool that you can use to create download or upload jobs and monitor their progress.
ms.assetid: 686d2201-c142-4e1c-a2b1-347d9334caa8
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BITSAdmin Tool

BITSAdmin is a command-line tool that you can use to create download or upload jobs and monitor their progress.

The \\Support\\Tools\\Support.cab file on the operating system installation CD contains the BITSAdmin tool. To unpack and install BITSAdmin, run the Setup. exe file in the Tools directory. If you do not have access to the installation CD, you can download the support tools from [Windows XP Service Pack 2 Support Tools](http://go.microsoft.com/fwlink/p/?linkid=84085).

The BITSAdmin tool uses switches to identify the work to perform. Most switches require a *Job* parameter that you set to the job's display name or GUID. Note that a job's display name may not be unique. The **/create** and **/list** switches return a job's GUID.

By default, you can access information about your own jobs. To access information for another user's jobs, you must have administrator privileges. If the job was created in an elevated state, you must run BitsAdmin from an elevated window; otherwise, you will have read-only access to the job.

Many of the switches correspond to methods in the [BITS interfaces](bits-interfaces.md). For additional details that may be relevant to using a switch, see the corresponding method.

Use the following switches to create a job, set and retrieve the properties of a job, and monitor the status of a job. For examples that show how to use some of these switches to perform tasks, see [BITSAdmin Examples](bitsadmin-examples.md).

<dl> <dt>

<span id="__________AddFile__________Job_RemoteURL_LocalName________"></span><span id="__________addfile__________job_remoteurl_localname________"></span><span id="__________ADDFILE__________JOB_REMOTEURL_LOCALNAME________"></span> **/AddFile** *Job RemoteURL LocalName* 
</dt> <dd>

Adds a file to the specified job. *RemoteURL* is the URL of the file on the server. *LocalName* is the name of the file on the local computer. *LocalName* must contain an absolute path to the file.

</dd> <dt>

<span id="_AddFileSet_Job_TextFile"></span><span id="_addfileset_job_textfile"></span><span id="_ADDFILESET_JOB_TEXTFILE"></span>**/AddFileSet** *Job TextFile*
</dt> <dd>

Adds one or more files to the specified job. Each line in *TextFile* contains a remote and local file name. The names are space-delimited. Lines that begin with a \# character are treated as a comment.

</dd> <dt>

<span id="__________AddFileWithRanges__________Job_RemoteURL_LocalName_RangeList________"></span><span id="__________addfilewithranges__________job_remoteurl_localname_rangelist________"></span><span id="__________ADDFILEWITHRANGES__________JOB_REMOTEURL_LOCALNAME_RANGELIST________"></span> **/AddFileWithRanges** *Job RemoteURL LocalName RangeList* 
</dt> <dd>

Adds a file to the specified job. BITS downloads the specified ranges from the remote file. Switch is valid only for download jobs. *RemoteURL* is the URL of the file on the server. *LocalName* is the name of the file on the local computer. *LocalName* must contain an absolute path to the file.

*RangeList* is a comma-delimited list of offset:length pairs. For example, the following range list tells BITS to transfer 100 bytes from offset 0, 100 bytes from offset 2000, and the remaining bytes from offset 5000 to the end of the file.

0:100,2000:100,5000:eof

</dd> <dt>

<span id="_Cancel_Job"></span><span id="_cancel_job"></span><span id="_CANCEL_JOB"></span>**/Cancel** *Job*
</dt> <dd>

Removes the job from the transfer queue and deletes all temporary files associated with the job.

</dd> <dt>

<span id="_Complete_Job"></span><span id="_complete_job"></span><span id="_COMPLETE_JOB"></span>**/Complete Job**
</dt> <dd>

Completes the job. The downloaded files are not available to you until you use this switch. Use this switch after the job moves to the transferred state. Otherwise, only those files that have been successfully transferred are available.

</dd> <dt>

<span id="__________Create__type_DisplayName________"></span><span id="__________create__type_displayname________"></span><span id="__________CREATE__TYPE_DISPLAYNAME________"></span> **/Create** \[**/type**\] *DisplayName* 
</dt> <dd>

Creates a transfer job with the given *DisplayName*. You can specify **/Download**, **/Upload**, or **/Upload-Reply** for the *type* parameter. The default type is **/Download**.

**BITS 1.2 and earlier:** The **/Upload** and **/Upload-Reply** types are not available.

Download jobs transfer data from a server to a local file. Upload jobs transfer data from a local file to a server. Upload-reply jobs transfer data from a local file to a server and receive a reply file from the server.

Use the **/resume** switch to activate the job in the transfer queue.

</dd> <dt>

<span id="_GetAclFlags_Job"></span><span id="_getaclflags_job"></span><span id="_GETACLFLAGS_JOB"></span>**/GetAclFlags** *Job*
</dt> <dd>

Retrieves the ACL propagations flags. Displays one or more of the following flag values:

-   O — Copy owner information with file.
-   G — Copy group information with file.
-   D — Copy DACL information with file.
-   S — Copy SACL information with file.

</dd> <dt>

<span id="_GetBytesTotal_Job"></span><span id="_getbytestotal_job"></span><span id="_GETBYTESTOTAL_JOB"></span>**/GetBytesTotal** *Job*
</dt> <dd>

Retrieves the size of the specified job.

</dd> <dt>

<span id="_GetBytesTransferred_Job"></span><span id="_getbytestransferred_job"></span><span id="_GETBYTESTRANSFERRED_JOB"></span>**/GetBytesTransferred** *Job*
</dt> <dd>

Retrieves the number of bytes transferred for the specified job.

</dd> <dt>

<span id="_GetCompletionTime_Job"></span><span id="_getcompletiontime_job"></span><span id="_GETCOMPLETIONTIME_JOB"></span>**/GetCompletionTime** *Job*
</dt> <dd>

Retrieves the time that the job finished transferring data.

</dd> <dt>

<span id="_GetCreationTime_Job"></span><span id="_getcreationtime_job"></span><span id="_GETCREATIONTIME_JOB"></span>**/GetCreationTime** *Job*
</dt> <dd>

Retrieves the job creation time for the specified job.

</dd> <dt>

<span id="_GetDescription_Job"></span><span id="_getdescription_job"></span><span id="_GETDESCRIPTION_JOB"></span>**/GetDescription** *Job*
</dt> <dd>

Retrieves the description of the specified job.

</dd> <dt>

<span id="_GetDisplayName_Job"></span><span id="_getdisplayname_job"></span><span id="_GETDISPLAYNAME_JOB"></span>**/GetDisplayName** *Job*
</dt> <dd>

Retrieves the display name of the specified job.

</dd> <dt>

<span id="_GetError_Job"></span><span id="_geterror_job"></span><span id="_GETERROR_JOB"></span>**/GetError** *Job*
</dt> <dd>

Retrieves detailed error information for the specified job.

</dd> <dt>

<span id="_GetErrorCount_Job"></span><span id="_geterrorcount_job"></span><span id="_GETERRORCOUNT_JOB"></span>**/GetErrorCount** *Job*
</dt> <dd>

Retrieves a count of the number of times the specified job generated a transient error.

</dd> <dt>

<span id="_GetFilesTotal_Job"></span><span id="_getfilestotal_job"></span><span id="_GETFILESTOTAL_JOB"></span>**/GetFilesTotal** *Job*
</dt> <dd>

Retrieves the number of files in the specified job.

</dd> <dt>

<span id="_GetFilesTransferred_Job"></span><span id="_getfilestransferred_job"></span><span id="_GETFILESTRANSFERRED_JOB"></span>**/GetFilesTransferred** *Job*
</dt> <dd>

Retrieves the number of files transferred for the specified job.

</dd> <dt>

<span id="_GetHelperNotifyFlags_Job"></span><span id="_gethelpernotifyflags_job"></span><span id="_GETHELPERNOTIFYFLAGS_JOB"></span>**/GetHelperNotifyFlags** *Job*
</dt> <dd>

Returns the usage flags for a [helper token](helper-tokens-for-bits-transfer-jobs.md) that is associated with a BITS transfer job. Possible values include the following:

-   0x0001 — The helper token is used to open the local file of an upload job, to create or rename the temporary file of a download job, or to create or rename the reply file of an upload-reply job.
-   0x0002 —The helper token is used to open the remote file of a Server Message Block (SMB) upload or download job, or in response to an HTTP server or proxy challenge for implicit NTLM or Kerberos credentials. You must call **/SetCredentials** *Job TargetScheme* **NULL NULL** to allow the credentials to be sent over HTTP.

**BITS 3.0 and earlier:** Not supported.

</dd> <dt>

<span id="_GetHelperTokensID_JobID"></span><span id="_gethelpertokensid_jobid"></span><span id="_GETHELPERTOKENSID_JOBID"></span>**/GetHelperTokensID** *JobID*
</dt> <dd>

Returns the SID of a BITS transfer job’s [helper token](helper-tokens-for-bits-transfer-jobs.md) if one is set.

**BITS 3.0 and earlier:** Not supported.

</dd> <dt>

<span id="_GetMinRetryDelay_Job"></span><span id="_getminretrydelay_job"></span><span id="_GETMINRETRYDELAY_JOB"></span>**/GetMinRetryDelay** *Job*
</dt> <dd>

Retrieves the length of time, in seconds, that the service waits after encountering a transient error before trying to transfer the file.

</dd> <dt>

<span id="_GetModificationTime_Job"></span><span id="_getmodificationtime_job"></span><span id="_GETMODIFICATIONTIME_JOB"></span>**/GetModificationTime** *Job*
</dt> <dd>

Retrieves the last time the job was modified or data was successfully transferred.

</dd> <dt>

<span id="_GetNoProgressTimeout_Job"></span><span id="_getnoprogresstimeout_job"></span><span id="_GETNOPROGRESSTIMEOUT_JOB"></span>**/GetNoProgressTimeout** *Job*
</dt> <dd>

Retrieves the length of time, in seconds, that the service tries to transfer the file after a transient error occurs.

</dd> <dt>

<span id="_GetNotifyCmdLine_Job"></span><span id="_getnotifycmdline_job"></span><span id="_GETNOTIFYCMDLINE_JOB"></span>**/GetNotifyCmdLine** *Job*
</dt> <dd>

Retrieves the command-line command to execute when the job finishes transferring data.

**BITS 1.2 and earlier:** Not supported.

</dd> <dt>

<span id="_GetNotifyFlags_Job"></span><span id="_getnotifyflags_job"></span><span id="_GETNOTIFYFLAGS_JOB"></span>**/GetNotifyFlags** *Job*
</dt> <dd>

Retrieves the notify flags for the specified job. The job can contain one or more of the following notification flags.

-   0x0001 — Generate an event when all files in the job have been transferred.
-   0x0002 — Generate an event when an error occurs.
-   0x0004 — Disable notifications.
-   0x0008 — Generate an event when the job is modified or transfer progress is made.

</dd> <dt>

<span id="_GetNotifyInterface_Job"></span><span id="_getnotifyinterface_job"></span><span id="_GETNOTIFYINTERFACE_JOB"></span>**/GetNotifyInterface** *Job*
</dt> <dd>

Determines if the notify interface is registered for the specified job. Displays REGISTERED or UNREGISTERED.

</dd> <dt>

<span id="_GetOwner_Job"></span><span id="_getowner_job"></span><span id="_GETOWNER_JOB"></span>**/GetOwner** *Job*
</dt> <dd>

Retrieves the owner of the specified job.

</dd> <dt>

<span id="_GetPriority_Job"></span><span id="_getpriority_job"></span><span id="_GETPRIORITY_JOB"></span>**/GetPriority** *Job*
</dt> <dd>

Retrieves the priority of the specified job. The priority is either FOREGROUND, HIGH, NORMAL, LOW, or UNKNOWN.

</dd> <dt>

<span id="_GetProxyBypassList_Job"></span><span id="_getproxybypasslist_job"></span><span id="_GETPROXYBYPASSLIST_JOB"></span>**/GetProxyBypassList** *Job*
</dt> <dd>

Retrieves the proxy bypass list for the specified job. The bypass list contains the host names or IP addresses, or both, that are not to be routed through a proxy. The list can contain "<local>" to refer to all servers on the same LAN. The list is space-delimited.

</dd> <dt>

<span id="_GetProxyList_Job"></span><span id="_getproxylist_job"></span><span id="_GETPROXYLIST_JOB"></span>**/GetProxyList** *Job*
</dt> <dd>

Retrieves the proxy list for the specified job. The proxy list is the list of proxy servers to use. The list is comma-delimited.

</dd> <dt>

<span id="_GetProxyUsage_Job"></span><span id="_getproxyusage_job"></span><span id="_GETPROXYUSAGE_JOB"></span>**/GetProxyUsage** *Job*
</dt> <dd>

Retrieves the proxy usage setting for the specified job. The possible values are:

-   PRECONFIG — Use the owner's Internet Explorer defaults.
-   NO\_PROXY —Do not use a proxy server.
-   OVERRIDE — Use an explicit proxy list.

</dd> <dt>

<span id="_GetReplyData_Job"></span><span id="_getreplydata_job"></span><span id="_GETREPLYDATA_JOB"></span>**/GetReplyData** *Job*
</dt> <dd>

Retrieves the server's reply data in hexadecimal format. Valid only for upload-reply jobs.

**BITS 1.2 and earlier:** Not supported.

</dd> <dt>

<span id="_GetReplyFileName_Job"></span><span id="_getreplyfilename_job"></span><span id="_GETREPLYFILENAME_JOB"></span>**/GetReplyFileName** *Job*
</dt> <dd>

Gets the path of the file that contains the server reply. Valid only for upload-reply jobs.

**BITS 1.2 and earlier:** Not supported.

</dd> <dt>

<span id="_GetReplyProgress_Job"></span><span id="_getreplyprogress_job"></span><span id="_GETREPLYPROGRESS_JOB"></span>**/GetReplyProgress** *Job*
</dt> <dd>

Retrieves the size and progress of the server reply. Valid only for upload-reply jobs.

**BITS 1.2 and earlier:** Not supported.

</dd> <dt>

<span id="_GetState_Job"></span><span id="_getstate_job"></span><span id="_GETSTATE_JOB"></span>**/GetState** *Job*
</dt> <dd>

Retrieves the state of the specified job. The possible states are:

-   QUEUED — The job is waiting to run.
-   CONNECTING — BITS is contacting the server.
-   TRANSFERRING — BITS is transferring data.
-   SUSPENDED — The job is paused.
-   ERROR — A nonrecoverable error occurred; the transfer will not be retried.
-   TRANSIENT\_ERROR — A recoverable error occurred; the transfer retries when the minimum retry delay expires.
-   ACKNOWLEDGED — The job was completed.
-   CANCELLED — The job was canceled.

</dd> <dt>

<span id="_GetType_Job"></span><span id="_gettype_job"></span><span id="_GETTYPE_JOB"></span>**/GetType** *Job*
</dt> <dd>

Retrieves the job type of the specified job. The type can be DOWNLOAD, UPLOAD, UPLOAD-REPLY, or UNKNOWN.

</dd> <dt>

<span id="_Help______"></span><span id="_help______"></span><span id="_HELP______"></span>**/Help \| /?** 
</dt> <dd>

Displays the command-line usage.

</dd> <dt>

<span id="__________Info__________Job___________verbose________"></span><span id="__________info__________job___________verbose________"></span><span id="__________INFO__________JOB___________VERBOSE________"></span> **/Info** *Job* \[**/verbose**\] 
</dt> <dd>

Displays summary information about the specified job. Use the */verbose* parameter to provide detailed information about the job.

</dd> <dt>

<span id="__________List___________allusers___________verbose________"></span><span id="__________list___________allusers___________verbose________"></span><span id="__________LIST___________ALLUSERS___________VERBOSE________"></span> **/List** \[**/allusers**\] \[**/verbose**\] 
</dt> <dd>

Lists the transfer jobs owned by the current user. To list jobs for all users, include the */allusers* parameter. You must have administrator privileges to use the */allusers* parameter. Use the */verbose* parameter to provide detailed information about jobs.

</dd> <dt>

<span id="_ListFiles_Job"></span><span id="_listfiles_job"></span><span id="_LISTFILES_JOB"></span>**/ListFiles** *Job*
</dt> <dd>

Lists the files in the specified job.

</dd> <dt>

<span id="_Monitor__allusers___refresh_Seconds"></span><span id="_monitor__allusers___refresh_seconds"></span><span id="_MONITOR__ALLUSERS___REFRESH_SECONDS"></span>**/Monitor** \[**/allusers**\] \[**/refresh Seconds**\]
</dt> <dd>

Monitors jobs in the transfer queue that the current user owns. To monitor jobs for all users, include the */allusers* parameter. You must have administrator privileges to use the allusers parameter. The */refresh* parameter refreshes the data at an interval specified by **Seconds**. The default refresh period is every 5 seconds. To stop the refresh, enter CTRL+C.

</dd> <dt>

<span id="_NoWrap"></span><span id="_nowrap"></span><span id="_NOWRAP"></span>**/NoWrap**
</dt> <dd>

Does not wrap output to fit in a command window. By default, all switches, except the /Monitor switch, wrap the output. Specify before other switches.

</dd> <dt>

<span id="_RawReturn"></span><span id="_rawreturn"></span><span id="_RAWRETURN"></span>**/RawReturn**
</dt> <dd>

Returns data suitable for parsing. Strips new line characters and formatting from the output. Typically, you use this switch in conjunction with the /create and /get\* switches to receive only the value. Specify before other switches.

</dd> <dt>

<span id="_RemoveCredentials_Job_Target_Scheme"></span><span id="_removecredentials_job_target_scheme"></span><span id="_REMOVECREDENTIALS_JOB_TARGET_SCHEME"></span>**/RemoveCredentials** *Job Target Scheme*
</dt> <dd>

Removes credentials from a job. Target can be either SERVER or PROXY. Scheme can be BASIC, DIGEST, NTLM, NEGOTIATE, or PASSPORT.

**BITS 1.2 and earlier:** Not supported.

</dd> <dt>

<span id="_ReplaceRemotePrefix_Job_OldPrefix_NewPrefix"></span><span id="_replaceremoteprefix_job_oldprefix_newprefix"></span><span id="_REPLACEREMOTEPREFIX_JOB_OLDPREFIX_NEWPREFIX"></span>**/ReplaceRemotePrefix** *Job OldPrefix NewPrefix*
</dt> <dd>

All files in the job whose remote URL begins with *OldPrefix* are changed to use *NewPrefix*.

</dd> <dt>

<span id="_Reset__AllUsers"></span><span id="_reset__allusers"></span><span id="_RESET__ALLUSERS"></span>**/Reset /AllUsers**
</dt> <dd>

Cancels all jobs in the transfer queue that the current user owns. If you have administrator privileges, you can specify /AllUsers to cancel all jobs in the queue.

**BITSAdmin 1.5 and earlier:** If you have administrator privileges, **Reset** cancels all jobs in the queue. The /AllUsers option is not supported.

</dd> <dt>

<span id="_Resume_Job"></span><span id="_resume_job"></span><span id="_RESUME_JOB"></span>**/Resume** *Job*
</dt> <dd>

Activates a new or suspended job in the transfer queue.

</dd> <dt>

<span id="_SetAclFlags_Job_flags"></span><span id="_setaclflags_job_flags"></span><span id="_SETACLFLAGS_JOB_FLAGS"></span>**/SetAclFlags** *Job flags*
</dt> <dd>

Sets the ACL propagations flags for the job. The flags indicate that you want to maintain the owner and ACL information with the file being downloaded. Specify one or more of the following flags. For example, to maintain the owner and group with the file, set *flags* to OG.

-   O — Copy owner information with file.
-   G — Copy group information with file.
-   D — Copy DACL information with file.
-   S — Copy SACL information with file.

</dd> <dt>

<span id="_SetCredentials_Job_Target_Scheme_UserName_Password"></span><span id="_setcredentials_job_target_scheme_username_password"></span><span id="_SETCREDENTIALS_JOB_TARGET_SCHEME_USERNAME_PASSWORD"></span>**/SetCredentials** *Job Target Scheme UserName Password*
</dt> <dd>

Adds credentials to a job. Target can be either SERVER or PROXY. Scheme can be BASIC, DIGEST, NTLM, NEGOTIATE, or PASSPORT.

**BITS 1.2 and earlier:** Not supported.

</dd> <dt>

<span id="_SetDescription_Job_Description"></span><span id="_setdescription_job_description"></span><span id="_SETDESCRIPTION_JOB_DESCRIPTION"></span>**/SetDescription** *Job Description*
</dt> <dd>

Sets the description of the specified job.

</dd> <dt>

<span id="_SetDisplayName_Job_DisplayName"></span><span id="_setdisplayname_job_displayname"></span><span id="_SETDISPLAYNAME_JOB_DISPLAYNAME"></span>**/SetDisplayName** *Job DisplayName*
</dt> <dd>

Sets the DisplayName of the specified job.

</dd> <dt>

<span id="_SetHelperToken_JobID"></span><span id="_sethelpertoken_jobid"></span><span id="_SETHELPERTOKEN_JOBID"></span>**/SetHelperToken** *JobID*
</dt> <dd>

Sets the current command prompt’s primary token as a BITS transfer job’s [helper token](helper-tokens-for-bits-transfer-jobs.md).

**BITS 3.0 and earlier:** Not supported.

</dd> <dt>

<span id="_SetHelperToken_JobID_username_domain_password_"></span><span id="_sethelpertoken_jobid_username_domain_password_"></span><span id="_SETHELPERTOKEN_JOBID_USERNAME_DOMAIN_PASSWORD_"></span>**/SetHelperToken** *JobID username@domain password* 
</dt> <dd>

Sets an arbitrary local user account’s token as a BITS transfer job’s [helper token](helper-tokens-for-bits-transfer-jobs.md).

**BITS 3.0 and earlier:** Not supported.

</dd> <dt>

<span id="_SetHelperTokenFlags_Job_Flags_"></span><span id="_sethelpertokenflags_job_flags_"></span><span id="_SETHELPERTOKENFLAGS_JOB_FLAGS_"></span>**/SetHelperTokenFlags** *Job Flags* 
</dt> <dd>

Sets the usage flags for a [helper token](helper-tokens-for-bits-transfer-jobs.md) that is associated with a BITS transfer job. Possible values include the following:

-   0x0001 — The helper token is used to open the local file of an upload job, to create or rename the temporary file of a download job, or to create or rename the reply file of an upload-reply job.
-   0x0002 —The helper token is used to open the remote file of a Server Message Block (SMB) upload or download job, or in response to an HTTP server or proxy challenge for implicit NTLM or Kerberos credentials. You must call **/SetCredentials** *Job TargetScheme* **NULL NULL** to allow the credentials to be sent over HTTP.

**BITS 3.0 and earlier:** Not supported.

</dd> <dt>

<span id="_SetMinRetryDelay_Job_Flags"></span><span id="_setminretrydelay_job_flags"></span><span id="_SETMINRETRYDELAY_JOB_FLAGS"></span>**/SetMinRetryDelay** *Job* *Flags*
</dt> <dd>

Sets the minimum length of time, in seconds, that BITS waits after encountering a transient error before trying to transfer the file.

</dd> <dt>

<span id="_SetNoProgressTimeout_Job_Time-out"></span><span id="_setnoprogresstimeout_job_time-out"></span><span id="_SETNOPROGRESSTIMEOUT_JOB_TIME-OUT"></span>**/SetNoProgressTimeout** *Job Time-out*
</dt> <dd>

Sets the length of time, in seconds, that BITS tries to transfer the file after the first transient error occurs.

</dd> <dt>

<span id="_SetNotifyCmdLine_Job_Program_NameProgram_Parameters"></span><span id="_setnotifycmdline_job_program_nameprogram_parameters"></span><span id="_SETNOTIFYCMDLINE_JOB_PROGRAM_NAMEPROGRAM_PARAMETERS"></span>**/SetNotifyCmdLine** *Job Program\_Name*\[**Program\_Parameters**\]
</dt> <dd>

Specify a command-line program to execute when the job finishes transferring data or is in error. You can specify **NULL** for Program\_Name and Program\_Parameters. If Program\_Name is **NULL**, Program\_Parameters must be **NULL**.

**BITS 1.2 and earlier:** Not supported.

The following examples show how to use this switch:

**bitsadmin** **/SetNotifyCmdLine** *MyJob* *C:\\Winnt\\System32\\Notepad.exe NULL*

**bitsadmin** **/SetNotifyCmdLine** *MyJob C:\\Handler.exe "C:\\Handler.exe parm1 parm2 parm3"*

**bitsadmin** **/SetNotifyCmdLine** *MyJob NULL NULL*

</dd> <dt>

<span id="_SetNotifyFlags_Job_NotifyFlags"></span><span id="_setnotifyflags_job_notifyflags"></span><span id="_SETNOTIFYFLAGS_JOB_NOTIFYFLAGS"></span>**/SetNotifyFlags** *Job NotifyFlags*
</dt> <dd>

Sets the event notification flags for the specified job. Specify one or more of the following notification flags. For example, to specify transferred and error events, set NotifyFlags to 0x0003.

-   0x0001 — Generate an event when all files in the job have been transferred.
-   0x0002 — Generate an event when an error occurs.
-   0x0004 — Disable notifications.
-   0x0008 — Generate an event when the job is modified or transfer progress is made.

</dd> <dt>

<span id="_SetPriority_Job_Priority"></span><span id="_setpriority_job_priority"></span><span id="_SETPRIORITY_JOB_PRIORITY"></span>**/SetPriority** *Job Priority*
</dt> <dd>

Sets the priority of the specified job. The priority must be either FOREGROUND, HIGH, NORMAL, or LOW.

</dd> <dt>

<span id="_SetProxySettings_Job_usage_List_Bypass"></span><span id="_setproxysettings_job_usage_list_bypass"></span><span id="_SETPROXYSETTINGS_JOB_USAGE_LIST_BYPASS"></span>**/SetProxySettings** *Job usage List Bypass*
</dt> <dd>

Sets the proxy settings for the specified job. The *usage* parameter can be one of the following values:

-   PRECONFIG — Use the owner's Internet Explorer defaults.
-   NO\_PROXY — Do not use a proxy server.
-   OVERRIDE — Use an explicit proxy list and bypass list. A proxy and proxy bypass list must follow.

The *List* parameter contains a comma-delimited list of proxy servers to use. The *Bypass* parameter contains a space-delimited list of host names or IP addresses, or both, for which transfers are not to be routed through a proxy. This can be <local> to refer to all servers on the same LAN. Values of **NULL** or "" may be used for an empty proxy bypass list.

The following examples show possible uses of the switch:

**bitsadmin** **/setproxysettings** *MyJob PRECONFIG*

**bitsadmin** **/setproxysettings** *MyJob NO\_PROXY*

**bitsadmin** **/setproxysettings** *MyJob OVERRIDE proxy1:80 "<local>"*

**bitsadmin** **/setproxysettings** *MyJob OVERRIDE proxy1,proxy2,proxy3 NULL*

</dd> <dt>

<span id="_SetReplyFileName_Job_Path"></span><span id="_setreplyfilename_job_path"></span><span id="_SETREPLYFILENAME_JOB_PATH"></span>**/SetReplyFileName** *Job Path*
</dt> <dd>

Specify the path of the file that contains the server reply. Valid only for upload-reply jobs.

**BITS 1.2 and earlier:** Not supported.

</dd> <dt>

<span id="_Suspend_Job"></span><span id="_suspend_job"></span><span id="_SUSPEND_JOB"></span>**/Suspend** *Job*
</dt> <dd>

Suspends the specified job. To restart the job, use the **/resume** switch.

</dd> <dt>

<span id="_TakeOwnership_Job"></span><span id="_takeownership_job"></span><span id="_TAKEOWNERSHIP_JOB"></span>**/TakeOwnership** *Job*
</dt> <dd>

Lets a user with administrative privileges take ownership of the specified job.

</dd> <dt>

<span id="__________Transfer__________name__________type___________priority_job_priority___________ACLFlags_flags__________remote_name_local_name________"></span><span id="__________transfer__________name__________type___________priority_job_priority___________aclflags_flags__________remote_name_local_name________"></span><span id="__________TRANSFER__________NAME__________TYPE___________PRIORITY_JOB_PRIORITY___________ACLFLAGS_FLAGS__________REMOTE_NAME_LOCAL_NAME________"></span> **/Transfer** *name* \[**type**\] \[**/priority job\_priority**\] \[**/ACLFlags flags**\] *remote\_name local\_name* 
</dt> <dd>

Transfers one or more files. By default, BITSAdmin creates a download job that runs at NORMAL priority. BITSAdmin updates the command window with progress information until the transfer is complete or until a critical error occurs. BITSAdmin completes the job if it successfully transfers all the files and cancels the job if a critical error occurs. BITSAdmin does not create the job if it is unable to add files to the job or if you specify an invalid value for *type* or *job\_priority*. Note that BITSAdmin continues to run if a transient error occurs. To end BITSAdmin, press Ctrl+C.

Use the *name* parameter to specify the name of the job.

The *type* parameter is optional. Use the *type* parameter to specify the type of job. Specify /download for a download job or /upload for an upload job.

The */priority* parameter is optional. To specify the priority of the job, set the *job\_priority* operand to FOREGROUND, HIGH, NORMAL, or LOW.

The */ACLFlags* parameter is optional. The flags indicate that you want to maintain the owner and ACL information with the file being downloaded. Specify one or more of the following flags. For example, to maintain the owner and group with the file, set *flags* to OG.

-   O — Copy owner information with file.
-   G — Copy group information with file.
-   D — Copy DACL information with file.
-   S — Copy SACL information with file.

To transfer more than one file, specify multiple remote\_name-local\_name pairs. The pairs are space-delimited.

</dd> <dt>

<span id="_Util__Help"></span><span id="_util__help"></span><span id="_UTIL__HELP"></span>**/Util /Help**
</dt> <dd>

Displays the command-line usage for the **/Util** switches. You can also specify **/?**.

**BITSAdmin 1.5 and earlier:** Not supported.

</dd> <dt>

<span id="_Util__GetIEProxy__Account__Conn__Connection_Name_"></span><span id="_util__getieproxy__account__conn__connection_name_"></span><span id="_UTIL__GETIEPROXY__ACCOUNT__CONN__CONNECTION_NAME_"></span>**/Util /GetIEProxy** *<Account>*\[**/Conn <Connection Name>**\]
</dt> <dd>

Retrieves the proxy usage for the given service account. This switch shows the value for each proxy usage, not just the proxy usage you specified for the service account.

Use the *<account>* parameter to specify the service account whose proxy settings you want to retrieve. Possible values are:

-   LOCALSYSTEM
-   NETWORKSERVICE
-   LOCALSERVICE

Use the */conn* parameter to specify the modem connection to use. If you do not specify the /conn parameter, BITS uses the LAN connection. Specify the modem connection name immediately following the /conn parameter.

For details on setting the proxy usage for service accounts, see the **/Util /SetIEProxy** switch.

</dd> <dt>

<span id="_Util__RepairService"></span><span id="_util__repairservice"></span><span id="_UTIL__REPAIRSERVICE"></span>**/Util /RepairService**
</dt> <dd>

If BITS fails to start, use this switch to fix known issues with various versions of BITS. For example, this switch resolves errors related to incorrect service configuration and dependencies on LANManworkstation service and the network directory. This switch generates output that indicates the issues that were resolved.

**BITSAdmin 1.5 and earlier:** Not supported.

Note that if BITS recreates the service, the service description string may be set to English in a localized system.

</dd> <dt>

<span id="_Util__SetIEProxy___Account___Usage___Conn__Connection_Name_"></span><span id="_util__setieproxy___account___usage___conn__connection_name_"></span><span id="_UTIL__SETIEPROXY___ACCOUNT___USAGE___CONN__CONNECTION_NAME_"></span>**/Util /SetIEProxy** *<Account> <Usage>* \[**/Conn <Connection Name>**\]
</dt> <dd>

Specify proxy settings to use when transferring files using a service account.

**BITSAdmin 1.5 and earlier:** Not supported.

Use the <account> parameter to specify the type of service account whose proxy usage you want to define. Possible values are:

-   LOCALSYSTEM
-   NETWORKSERVICE
-   LOCALSERVICE

Use the <usage> parameter to specify the form of proxy detection to use. Possible values are:

-   NO\_PROXY—Do not use a proxy server.
-   AUTODETECT—Automatically detect the proxy settings.
-   MANUAL\_PROXY—Use an explicit proxy list and bypass list. Specify the proxy list and bypass list immediately following the usage tag. For example, MANUAL\_PROXY proxy1,proxy2 **NULL**.

    The proxy list is a comma-delimited list of proxy servers to use.

    The bypass list is a space-delimited list of host names or IP addresses, or both, for which transfers are not to be routed through a proxy. This can be <local> to refer to all servers on the same LAN. Values of **NULL** or "" may be used for an empty proxy bypass list.

-   AUTOSCRIPT—Same as AUTODETECT, except it also executes a script. Specify the script URL immediately following the usage tag. For example, AUTOSCRIPT http://server/proxy.js.
-   RESET—Same as NO\_PROXY, except it removes the manual proxy URLs (if specified) and URLs discovered using automatic detection.

Note that each successive call using this switch does not replace the previously specified usage. For example, if you specify NO\_PROXY, AUTODETECT, and MANUAL\_PROXY on separate calls, BITS uses automatic detection to determine the proxy to use. If automatic detection fails, BITS uses MANUAL\_PROXY.

Use the /conn parameter to specify the modem connection to use. If you do not specify the /conn parameter, BITS uses the LAN connection. Specify the modem connection name immediately following the /conn parameter.

The following examples show how to use the **/Util /SetIEProxy** switch:

**bitsadmin** **/util /setieproxy** *localsystem* **AUTODETECT**

**bitsadmin** **/util /setieproxy** *localsystem* **MANUAL\_PROXY proxy1,proxy2,proxy3 NULL**

**bitsadmin** **/util /setieproxy** *localsystem* **MANUAL\_PROXY proxy1:80 "<local>"**

</dd> <dt>

<span id="_Util__Version__Verbose"></span><span id="_util__version__verbose"></span><span id="_UTIL__VERSION__VERBOSE"></span>**/Util /Version** \[**/Verbose**\]
</dt> <dd>

Displays the version of BITS (for example 2.0) that is running. Use the verbose option to display information about the state of BITS.

**BITSAdmin 1.5 and earlier:** Not supported.

</dd> <dt>

<span id="_Wrap"></span><span id="_wrap"></span><span id="_WRAP"></span>**/Wrap**
</dt> <dd>

Wraps output to fit in a command window. Specify before other switches. By default, all switches, except the /Monitor switch, wrap the output.

</dd> </dl>

 

 




