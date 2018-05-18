---
Description: 'Users using .NET can use rowsets to access a subset of an object's properties. Retrieving a subset of the object's properties provides better performance over retrieving the full object.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9047cffc-71f3-4c4a-a387-2807802af1a7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Using a Rowset to Enumerate a List of Objects
---

# Using a Rowset to Enumerate a List of Objects

Users using .NET can use rowsets to access a subset of an object's properties. Retrieving a subset of the object's properties provides better performance over retrieving the full object. However, rowsets are read-only, so if you need to update the job, you will still need to retrieve the object.

You can use the following methods to retrieve rowsets:

-   [**IScheduler.OpenJobEnumerator**](frlrfMicrosoftHpcSchedulerISchedulerClassOpenJobEnumeratorTopic)
-   [**IScheduler.OpenJobHistoryEnumerator**](frlrfMicrosoftHpcSchedulerISchedulerClassOpenJobHistoryEnumeratorTopic)
-   [**IScheduler.OpenJobRowSet**](frlrfMicrosoftHpcSchedulerISchedulerClassOpenJobRowSetTopic)
-   [**IScheduler.OpenNodeEnumerator**](frlrfMicrosoftHpcSchedulerISchedulerClassOpenNodeEnumeratorTopic)
-   [**IScheduler.OpenNodeHistoryEnumerator**](frlrfMicrosoftHpcSchedulerISchedulerClassOpenNodeHistoryEnumeratorTopic)
-   [**ISchedulerJob.OpenTaskEnumerator**](frlrfMicrosoftHpcSchedulerISchedulerJobClassOpenTaskEnumeratorTopic)
-   [**ISchedulerJob.OpenTaskRowSet**](frlrfMicrosoftHpcSchedulerISchedulerJobClassOpenTaskRowSetTopic)

Note that the rowset will time out and throw an exception if you try to access data from the rowset after the rowset has been idle for more than one minute (the rowset expires if you do not retrieve data from the rowset for more than one minute; the timer is reset every time you retrieve data).

For an example that shows how to test for null property values, see [Checking for Null Property Values](checking-for-null-property-values.md).

The following C# example shows how to use a rowset enumerator to get a set of properties for a specific job.


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;

namespace Using_a_Rowset_to_Enumerate_a_List_of_Objects
{
    class Program
    {
        static void Main(string[] args)
        {
            IScheduler scheduler = new Scheduler();

            try
            {
                scheduler.Connect("localhost");

                GetSingleJobUsingEnumerator(scheduler);
                GetJobsUsingEnumerator(scheduler);
                GetJobsUsingEnumerator2(scheduler);
                GetSingleJobUsingRowset(scheduler);
                GetJobsUsingRowset(scheduler);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }


        // Shows how to use a rowset enumerator to retrieve a single job. The example 
        // uses a filter to retrieve the specified properties for a single job.
        static void GetSingleJobUsingEnumerator(IScheduler scheduler)
        {
            ISchedulerRowEnumerator rowset = null;
            PropertyRowSet rows = null;
            PropertyRow row = null;
            IPropertyIdCollection properties = new PropertyIdCollection();
            IFilterCollection filters = scheduler.CreateFilterCollection();

            // Specify the properties to include for each job in the enumerator.
            properties.Add(JobPropertyIds.Id);
            properties.Add(JobPropertyIds.AllocatedCores);
            properties.Add(JobPropertyIds.AllocatedNodes);
            properties.Add(JobPropertyIds.AllocatedSockets);

            // Specify one or more filters to use to select the jobs to include in the enumerator.
            filters.Add(FilterOperator.Equal, JobPropertyIds.Id, 5);

            // Get an enumerator that contains all the jobs that match the filter criteria.
            // In this case, the enumerator should contain a single job if it exists.
            using (rowset = scheduler.OpenJobEnumerator(properties, filters, null))
            {
                Console.WriteLine("\nUsing OpenJobEnumerator to retrieve data for a single job...");

                // Get a rowset from the enumerator that contains the single job.
                rows = rowset.GetRows(1);

                // If the job exists, get the job from the rowset and retrieve the requested property data.
                if (rows.Length == 0)
                    Console.WriteLine("Job not found");
                else
                {
                    row = rows.Rows[0];

                    Console.WriteLine("Job " + (int)row[JobPropertyIds.Id].Value);

                    // Key is the node name; value is always 1.
                    Console.WriteLine("AllocatedNodes: ");
                    foreach (KeyValuePair<string, int> node in (List<KeyValuePair<string, int>>)row[JobPropertyIds.AllocatedNodes].Value)
                        Console.Write(node.Key + " ");
                    Console.WriteLine();

                    // Key is the node name; value is the number of cores on the node allocated to the job.
                    Console.WriteLine("AllocatedCores: ");
                    foreach (KeyValuePair<string, int> node in (List<KeyValuePair<string, int>>)row[JobPropertyIds.AllocatedCores].Value)
                        Console.Write("{0}({1})", node.Key, node.Value);
                    Console.WriteLine();

                    // Key is the node name; value is the number of sockets on the node allocated to the job.
                    Console.WriteLine("AllocatedSockets: ");
                    foreach (KeyValuePair<string, int> node in (List<KeyValuePair<string, int>>)row[JobPropertyIds.AllocatedSockets].Value)
                        Console.Write("{0}({1})", node.Key, node.Value);
                    Console.WriteLine();
                }
            }
        }


        // Shows how to use a rowset enumerator to retrieve the specified 
        // properties for all jobs that match the filter criteria. The example
        // uses a foreach loop to iterate through the results
        static void GetJobsUsingEnumerator(IScheduler scheduler)
        {
            ISchedulerRowEnumerator rows = null;
            IPropertyIdCollection properties = new PropertyIdCollection();
            IFilterCollection filters = scheduler.CreateFilterCollection();
            int jobCount = 0;

            // Specify the properties to include for each job in the enumerator.
            properties.Add(JobPropertyIds.Id);
            properties.Add(JobPropertyIds.AllocatedCores);
            properties.Add(JobPropertyIds.AllocatedNodes);
            properties.Add(JobPropertyIds.AllocatedSockets);

            // Specify one or more filters to use to select the jobs to include in the enumerator.
            filters.Add(FilterOperator.Equal, JobPropertyIds.State, JobState.Finished);

            // Get an enumerator that contains all the jobs that match the filter criteria.
            using (rows = scheduler.OpenJobEnumerator(properties, filters, null))
            {
                Console.WriteLine("Retrieving jobs using a rowset enumerator...");

                try
                {
                    // Iterate through the items in the enumerator.
                    foreach (PropertyRow row in rows)
                    {
                        Console.WriteLine("Job " + (int)row[JobPropertyIds.Id].Value);

                        // Key is the node name; value is always 1.
                        Console.WriteLine("AllocatedNodes: ");
                        foreach (KeyValuePair<string, int> node in (List<KeyValuePair<string, int>>)row[JobPropertyIds.AllocatedNodes].Value)
                            Console.Write(node.Key + " ");
                        Console.WriteLine();

                        // Key is the node name; value is the number of cores on the node allocated to the job.
                        Console.WriteLine("AllocatedCores: ");
                        foreach (KeyValuePair<string, int> node in (List<KeyValuePair<string, int>>)row[JobPropertyIds.AllocatedCores].Value)
                            Console.Write("{0}({1})", node.Key, node.Value);
                        Console.WriteLine();

                        // Key is the node name; value is the number of sockets on the node allocated to the job.
                        Console.WriteLine("AllocatedSockets: ");
                        foreach (KeyValuePair<string, int> node in (List<KeyValuePair<string, int>>)row[JobPropertyIds.AllocatedSockets].Value)
                            Console.Write("{0}({1})", node.Key, node.Value);
                        Console.WriteLine();

                        jobCount++;
                    }

                    if (0 == jobCount)
                        Console.WriteLine("No jobs found that match the filter criteria");
                }
                catch (Exception e)
                {
                    Console.WriteLine("\n" + e.Message + "\n" + e.StackTrace);
                }
            }
        }


        // Shows how to use a rowset enumerator to retrieve the specified 
        // properties for all jobs that match the filter criteria. The example
        // uses a while loop to fetch blocks of rows from the results.
        static void GetJobsUsingEnumerator2(IScheduler scheduler)
        {
            ISchedulerRowEnumerator rows = null;
            IPropertyIdCollection properties = new PropertyIdCollection();
            IFilterCollection filters = scheduler.CreateFilterCollection();

            // Specify the properties to include for each job in the enumerator.
            properties.Add(JobPropertyIds.Id);
            properties.Add(JobPropertyIds.AllocatedCores);
            properties.Add(JobPropertyIds.AllocatedNodes);
            properties.Add(JobPropertyIds.AllocatedSockets);

            // Specify one or more filters to use to select the jobs to include in the enumerator.
            filters.Add(FilterOperator.Equal, JobPropertyIds.State, JobState.Finished);

            // Get an enumerator that contains all the jobs that match the filter criteria.
            using (rows = scheduler.OpenJobEnumerator(properties, filters, null))
            {
                Console.WriteLine("Retrieving jobs using a rowset enumerator...");

                while (true)
                {
                    // Get a block of 128 rows from the enumerator.
                    PropertyRowSet set = rows.GetRows(128);

                    // If there are no more rows in the enumerator, exit the loop.
                    if (0 == set.Length)
                        break;

                    // Iterate through the rows in the block.
                    foreach (PropertyRow row in set.Rows)
                    {
                        Console.WriteLine("Job " + (int)row[JobPropertyIds.Id].Value);

                        // TODO: Print the allocated cores, nodes, and sockets.
                    }

                }
            }
        }

        // Shows how to use a rowset to retrieve a single job. The example 
        // shows how to use a filter to retrieve the specified properties for a single job.
        // It also shows how to use the GetObjectIndex method to select a single job
        // when the rowset contains more than one job.
        static void GetSingleJobUsingRowset(IScheduler scheduler)
        {
            ISchedulerRowSet rowset = null;
            PropertyRowSet rows = null;
            PropertyRow row = null;
            IPropertyIdCollection properties = new PropertyIdCollection();
            IFilterCollection filters = scheduler.CreateFilterCollection();

            // Specify the properties to include for each job in the rowset.
            properties.Add(JobPropertyIds.Id);
            properties.Add(JobPropertyIds.AllocatedCores);
            properties.Add(JobPropertyIds.AllocatedNodes);
            properties.Add(JobPropertyIds.AllocatedSockets);

            // Specify one or more filters to use to select the jobs to include in the rowset.
            filters.Add(FilterOperator.Equal, JobPropertyIds.Id, 5);

            // Get a rowset that contains all the jobs that match the filter criteria.
            // In this case, the rowset should contain a single job if it exists.
            using (rowset = scheduler.OpenJobRowSet(properties, filters, null))
            {
                Console.WriteLine("\nUsing OpenJobRowSet to retrieve data for a single job...");

                // Get a block of rows from the rowset that contains the single job.
                rows = rowset.GetRows(0, 0);

                // If the job exists, get the job from the block and retrieve the requested property data.
                if (rows.Length > 0)
                {
                    row = rows.Rows[0];

                    Console.WriteLine("Job " + (int)row[JobPropertyIds.Id].Value);

                    // TODO: Print the allocated cores, nodes, and sockets.
                }
            }

            // Create a new filter that returns all finished jobs.
            filters = scheduler.CreateFilterCollection();
            filters.Add(FilterOperator.Equal, JobPropertyIds.State, JobState.Finished);

            // Get a rowset that contains all the jobs that match the filer criteria.
            using (rowset = scheduler.OpenJobRowSet(properties, filters, null))
            {
                Console.WriteLine("\nUsing GetObjectIndex to retrieve a single job from a rowset...");

                int index = rowset.GetObjectIndex(5);

                // If the rowset includes the job, get the job from the rowset and retrieve the requested
                // property data. Index is -1 if the job is not found in the rowset.
                if (index >= 0)
                {
                    row = rowset.GetRows(index, index).Rows[0];

                    Console.WriteLine("Job " + (int)row[JobPropertyIds.Id].Value);

                    // TODO: Print the allocated cores, nodes, and sockets.
                }
            }
        }


        // Shows how to use a rowset to retrieve the specified 
        // properties for all jobs that match the filter criteria. The example
        // uses a while loop to fetch blocks of rows from the results.
        static void GetJobsUsingRowset(IScheduler scheduler)
        {
            ISchedulerRowSet rowset = null;
            IPropertyIdCollection properties = new PropertyIdCollection();
            IFilterCollection filters = scheduler.CreateFilterCollection();
            PropertyRowSet rows = null;
            int firstRow = 0;
            int lastRow = 127;
            Boolean firstBlock = true;

            // Specify the properties to include for each job in the rowset.
            properties.Add(JobPropertyIds.Id);
            properties.Add(JobPropertyIds.AllocatedCores);
            properties.Add(JobPropertyIds.AllocatedNodes);
            properties.Add(JobPropertyIds.AllocatedSockets);

            // Specify one or more filters to use to select the jobs to include in the enumerator.
            filters.Add(FilterOperator.Equal, JobPropertyIds.State, JobState.Finished);

            // Get a rowset that contains all the jobs that match the filter criteria.
            using (rowset = scheduler.OpenJobRowSet(properties, filters, null))
            {
                Console.WriteLine("Retrieving jobs using a rowset...");

                while (true)
                {
                    // Get a block of 128 rows from the rowset.
                    rows = rowset.GetRows(firstRow, lastRow);

                    // If there are no more rows in the rowset, exit the loop.
                    if (0 == rows.Length)
                    {
                        if (true == firstBlock)
                        {
                            Console.WriteLine("No jobs found that match the filter criteria");
                        }

                        break;
                    }
                    else
                    {
                        firstBlock = false;
                    }

                    // Iterate through the rows in the block.
                    foreach (PropertyRow row in rows.Rows)
                    {
                        Console.WriteLine("Job " + (int)row[JobPropertyIds.Id].Value);

                        // Key is the node name; value is always 1.
                        Console.WriteLine("AllocatedNodes: ");
                        foreach (KeyValuePair<string, int> node in (List<KeyValuePair<string, int>>)row[JobPropertyIds.AllocatedNodes].Value)
                            Console.Write(node.Key + " ");
                        Console.WriteLine();

                        // Key is the node name; value is the number of cores on the node allocated to the job.
                        Console.WriteLine("AllocatedCores: ");
                        foreach (KeyValuePair<string, int> node in (List<KeyValuePair<string, int>>)row[JobPropertyIds.AllocatedCores].Value)
                            Console.Write("{0}({1})", node.Key, node.Value);
                        Console.WriteLine();

                        // Key is the node name; value is the number of sockets on the node allocated to the job.
                        Console.WriteLine("AllocatedSockets: ");
                        foreach (KeyValuePair<string, int> node in (List<KeyValuePair<string, int>>)row[JobPropertyIds.AllocatedSockets].Value)
                            Console.Write("{0}({1})", node.Key, node.Value);
                        Console.WriteLine();
                    }

                    // Specify the next block of rows to get.
                    firstRow = lastRow;
                    lastRow += 127;
                }
            }
        }
    }
}
```



 

 



