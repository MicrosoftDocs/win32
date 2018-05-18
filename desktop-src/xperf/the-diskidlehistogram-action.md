---
title: The DiskIdleHistogram Action
description: The DiskIdleHistogram Action
ms.assetid: '52ffd7e4-4d2e-4add-8405-d26a5c109ef8'
---

# The DiskIdleHistogram Action

The DiskIdleHistogram action produces a text report that displays all disk activity and idle times in a histogram format.


```
Xperf -i Trace.etl -a diskidlehistogram -disknum N -buckets B1 B2 ... Bn   -idletimeout T1 T2 ... Tn   -idletheshold T   -spindownOverhead T     -spinupOverhead T
```



### DiskIdleHistogram Background and Terminology

The Xperf action DiskIdleHistogram is used to study the frequency of disk activity and idleness for each disk in a system. The information displayed in the DiskIdleHistogram enables the analyst to understand disk power usage for a specific time interval. More and longer idle periods can result in significantly lower power usage.

### Disk Idle Period:

The DiskIdleHistogram records disk Reads, Writes, and Flushes. A *disk idle period* is defined as the duration between the completion time of the previous disk IO and the start time of the current disk IO.

> [!Note]  
> Because IO requests may be queued, delayed or reordered, the start time refers to when an IO actually hits the physical disk, not when a disk IO is requested.

 

### Disk Idle Histogram:

A *Disk Idle Histogram* displays the distribution of disk idle time and the number of idle periods over different ranges of idle period length, as illustrated in the following table.



|                                  | &lt; 1 (s)      | 1 - 600 (s)     | &gt; 600 (s)    |
|----------------------------------|-----------------|-----------------|-----------------|
| Idle Time<br/>             | 1000<br/> | 1000<br/> | 2000<br/> |
| % of Total Idle Time<br/>  | 25<br/>   | 25<br/>   | 50<br/>   |
| Idle Count<br/>            | 90<br/>   | 5<br/>    | 5<br/>    |
| % of Total Idle Count<br/> | 90<br/>   | 5<br/>    | 5<br/>    |



 

-   The first row shows the histogram's buckets: different ranges of idle length.

-   The second row shows the accumulated idle time for each bucket. For example, the accumulated idle time for all idle periods shorter than 1 second is 1000 seconds.

-   The third row calculates the percentage of idle time for each bucket by dividing the idle time for a bucket by the total idle time.

-   The fourth row is the count of idle periods captured for each bucket. In this example, there are 90 idle periods lasting less than one second.

-   The last row calculates the percentage of idle periods for each bucket by dividing the number of idle periods for a bucket by the total number of idle periods.

### Per-File Idle Histogram:

The above Disk Idle Histogram includes disk IOs from all files. In order to further understand sources of disk IOs a histogram can be produced for each file. The "idle period" for a particular file is the duration between two neighboring disk IOs to this file. Disk IOs to all other files are ignored when producing the histogram for this file. These per-file histograms reflect the frequency of disk IOs to each file.

### Disk Idle Timeout:

This is the timeout to spin down a disk when the disk is idle. For example, if the timeout is 10 minutes, the disk will be spun down after it has been idle for 10 minutes.

### Disk Spindown Opportunity:

Using a sequence of disk IO timestamps and a given idle timeout, we can compute when the disk would be spun down and how much time it can stay in spun-down state, as illustrated in the following table.



| Timeout(s)                                        | 5               | 60              | 180             | 600            |
|---------------------------------------------------|-----------------|-----------------|-----------------|----------------|
| Estimated Spindown Opportunity Time(s)<br/> | 3800<br/> | 2000<br/> | 1000<br/> | 500<br/> |
| Estimated Spindown Opportunity Count<br/>   | 500<br/>  | 100<br/>  | 50<br/>   | 10<br/>  |



 

The first row shows the idle timeout values of interest for estimating spun down time. The second row shows the estimated total spun down time corresponding to each timeout. In this example, a timeout of 5 seconds yielded the total spun down time of 3800 seconds. The third row shows the estimated number of times the disk is spun down for each given timeout value.

### Capturing Disk Traces

For capturing an ETW trace to study disk idleness, we have two suggestions:

1.  Use a USB disk to collect data to avoid perturbing the disk under study.

2.  Collect information on disk IOs as well as related information, such as registry/cswitch/stacks, in case deeper analysis is needed. Compact\_cswitch can be used to reduce trace file size. The following shows a set of recommended Xperf flags:


```
xperf -on  dispatcher+PROC_THREAD+LOADER+CSWITCH+COMPACT_CSWITCH +registry+DISK_IO+DISK_IO_INIT+FILEIO -stackwalk cswitch+readythread+DiskReadInit+DiskWriteInit+DiskFlushInit  -buffersize 1024
sleep <desired trace time in seconds> or run scenario
xperf -d Trace.etl
```



### Post-Processing Disk Trace with DiskIdleHistogram Action

A typical usage of this action with default parameters is as follows:


```
Xperf  -i  Trace.etl -a diskidlehistogram > output.csv
```



The default parameter values are listed in the following table.



| Parameter                                                                | Default Value                                                                                 |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Disk number (0-based disk index)<br/>                              | output histograms for all disks <br/>                                                   |
| Histogram buckets <br/>                                            | &lt;1s, 1-5s, 5-60s, 60-180s, 180-600s, 600-900s, 900-1200s, 1200-1800s, &gt;1800s<br/> |
| Idle timeouts <br/>                                                | 5s, 60s, 180s, 600s, 1800s<br/>                                                         |
| Spin down overhead <br/>                                           | 0s<br/>                                                                                 |
| Spin up overhead <br/>                                             | 0s<br/>                                                                                 |
| Idle threshod(ignore idle periods shorter than this threshod)<br/> | 0s<br/>                                                                                 |



 

All these parameters are configurable using the following action options.


```
Xperf -i Trace.etl -a diskidlehistogram -disknum N -buckets B1 B2 ... Bn   -idletimeout T1 T2 ... Tn   -idletheshold T   -spindownOverhead T     -spinupOverhead T
```



### Output

**DiskIdleHistogram output imported into Microsoft Excel** shows an example output from this action. Histograms and related information are output for each disk if no disk index is specified. For each disk, the first section shows the count, size, service time (without IO queue time), and elapsed time (including IO queue time) for disk reads, writes, and flushes. The second section shows the idle histogram for the whole disk. The third section shows the estimates of spindown opportunity for different timeouts. The fourth section shows the per-file idle histogram and related information.

To figure out which files are the top hitters, use Microsoft Excel to sort rows based on how frequently disk IOs occur. We introduce two metrics for this, shown in the output:

-   **AvgIOInterval**: For particular file, this is the average interval between two neighboring IOs to this file. This metric may have problems when a file has tiny IO intervals, for example intervals less than one second. Even if this file also has large IO intervals, for example 30 minutes, the average IO interval may look much worse than another file with medium short IO intervals of about ten minutes. In this case, we may use the option -idlethreshold T to remove idle periods of less than one second from the analysis.

-   **MaxIOInterval**: For each file, this is the maximum interval between two neighboring IOs to this file. The output is sorted based on this metric by default. We should be cautious that a file with one large IO interval may still have frequent IOs on average. Looking at both metrics and per-file idle histograms would give us a more comprehensive and better understanding.

> [!Note]  
> Use both of these metrics and per-file histograms for a comprehensive picture of disk activity.

 

The following table shows the DiskIdleHistogram output imported into Excel.

![table showing the diskidlehistogram output imported into excel](images/dh-01.png)

### Advanced Usage: Ignoring Files

When we analyze disk activity sources, we often want to see the impact of one or more files on the overall idle histogram of the disk. We would ignore disk IOs to these files and see how the histogram changes. This can be done with one of the following options of this action.


```
Xperf  -i  Trace.etl -a diskidlehistogram -exc_file File1...   -exc_filestr Str1...   -exc_filere Expr1...
```



**-exc\_file** to ignore one or more full file paths, e.g., "C:\\Windows\\System32\\Config". With this option, you need to specify the full file path for each file you want to ignore.

**-exc\_filestr** to ignore files containing one or more strings, e.g., you can ignore any file paths containing string "C:\\Windows".

**-exc\_filere** to ignore files by ATL regular expressions, e.g., you can ignore all files ending with .dll by specifying a regular expression ".\*\\.dll".

It is important to note that there are a few system files whose disk IOs are in response to disk IOs to other files. These system files include:

**$LogFiles, $Mft, $Bitmap, lastalive0.dat, lastalive1.dat, $UsnJrnl:$ J**

It may be difficult to differentiate which disk IOs to other files cause which disk IOs to the above system files. Consequently, if you want to see the impact of the files you ignore, you also need to ignore these system files. Since these system files' disk IOs are in response to or piggyback with other disk IOs, ignoring only these system files themselves is not expected to change the disk idle histogram significantly.

 

 





