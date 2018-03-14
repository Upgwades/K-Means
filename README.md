# K-Means

A project developed to implement the machine learning k-means algorithm. Uses python 2.7.

### Running It

This section will explain the inputs and outputs of running the code. Use the provided csv to test the code.

#### Inputs

Full file location of a clean csv with useful data.

```
Enter file location: D:\...\dow_jones_index.data
```

Number of desired clusters.

```
Enter the number of desired clusters: 5
```

Many dataset include data not helpful to clustering. Use this option to ignore those columns.

```
Enter the numbers (comma seperated) of the attributes you would like to ignore: 1,3,5
```

#### Outputs

The following information is a sample of output.

```
For cluster 0:
It had 105 instances
and a final centroid at[ 64.86071777   3.72861004   0.18159799]

For cluster 1:
It had 200 instances
and a final centroid at[ 6.06869316 -0.0705302   0.504695  ]

For cluster 2:
It had 364 instances
and a final centroid at[-3.51829338  0.70679402  0.40650401]

For cluster 3:
It had 51 instances
and a final centroid at[ 5.59361839  0.19330917  0.69156408]

The algorithm took 3 iterations and had a total square error of 1702995.29199

```

## Authors

* **Will Irwin** - *Everything* - [Upgwades](https://github.com/Upgwades)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Stackoverflow was very helpful
* [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets.html)
