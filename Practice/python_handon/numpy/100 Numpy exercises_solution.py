{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ---------------------------------------------------------------\n",
    "# python best courses https://courses.tanpham.org/\n",
    "# ---------------------------------------------------------------\n",
    "\n",
    "# 100 numpy exercises\n",
    "\n",
    "This is a collection of exercises that have been collected in the numpy mailing list, on stack overflow and in the numpy documentation. The goal of this collection is to offer a quick reference for both old and new users but also to provide a set of exercices for those who teach."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 1. Import the numpy package under the name `np` (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 2. Print the numpy version and the configuration (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "print(np.__version__)\n",
    "np.show_config()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3. Create a null vector of size 10 (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.zeros(10)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 4.  How to find the memory size of any array (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.zeros((10,10))\n",
    "print(\"%d bytes\" % (Z.size * Z.itemsize))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 5.  How to get the documentation of the numpy add function from the command line? (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "%run `python -c \"import numpy; numpy.info(numpy.add)\"`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 6.  Create a null vector of size 10 but the fifth value which is 1 (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.zeros(10)\n",
    "Z[4] = 1\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 7.  Create a vector with values ranging from 10 to 49 (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.arange(10,50)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 8.  Reverse a vector (first element becomes last) (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.arange(50)\n",
    "Z = Z[::-1]\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 9.  Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.arange(9).reshape(3,3)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 10. Find indices of non-zero elements from \\[1,2,0,0,4,0\\] (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "nz = np.nonzero([1,2,0,0,4,0])\n",
    "print(nz)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 11. Create a 3x3 identity matrix (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.eye(3)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 12. Create a 3x3x3 array with random values (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.random((3,3,3))\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.random((10,10))\n",
    "Zmin, Zmax = Z.min(), Z.max()\n",
    "print(Zmin, Zmax)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 14. Create a random vector of size 30 and find the mean value (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.random(30)\n",
    "m = Z.mean()\n",
    "print(m)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.ones((10,10))\n",
    "Z[1:-1,1:-1] = 0\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.ones((5,5))\n",
    "Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 17. What is the result of the following expression? (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "print(0 * np.nan)\n",
    "print(np.nan == np.nan)\n",
    "print(np.inf > np.nan)\n",
    "print(np.nan - np.nan)\n",
    "print(0.3 == 3 * 0.1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.diag(1+np.arange(4),k=-1)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.zeros((8,8),dtype=int)\n",
    "Z[1::2,::2] = 1\n",
    "Z[::2,1::2] = 1\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "print(np.unravel_index(100,(6,7,8)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.tile( np.array([[0,1],[1,0]]), (4,4))\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 22. Normalize a 5x5 random matrix (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.random((5,5))\n",
    "Zmax, Zmin = Z.max(), Z.min()\n",
    "Z = (Z - Zmin)/(Zmax - Zmin)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "color = np.dtype([(\"r\", np.ubyte, 1),\n",
    "                  (\"g\", np.ubyte, 1),\n",
    "                  (\"b\", np.ubyte, 1),\n",
    "                  (\"a\", np.ubyte, 1)])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.dot(np.ones((5,3)), np.ones((3,2)))\n",
    "print(Z)\n",
    "\n",
    "# Alternative solution, in Python 3.5 and above\n",
    "Z = np.ones((5,3)) @ np.ones((3,2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Evgeni Burovski\n",
    "\n",
    "Z = np.arange(11)\n",
    "Z[(3 < Z) & (Z <= 8)] *= -1\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 26. What is the output of the following script? (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Jake VanderPlas\n",
    "\n",
    "print(sum(range(5),-1))\n",
    "from numpy import *\n",
    "print(sum(range(5),-1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z**Z\n",
    "2 << Z >> 2\n",
    "Z <- Z\n",
    "1j*Z\n",
    "Z/1/1\n",
    "Z<Z>Z"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 28. What are the result of the following expressions?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "print(np.array(0) / np.array(0))\n",
    "print(np.array(0) // np.array(0))\n",
    "print(np.array([np.nan]).astype(int).astype(float))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 29. How to round away from zero a float array ? (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Charles R Harris\n",
    "\n",
    "Z = np.random.uniform(-10,+10,10)\n",
    "print (np.copysign(np.ceil(np.abs(Z)), Z))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 30. How to find common values between two arrays? (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z1 = np.random.randint(0,10,10)\n",
    "Z2 = np.random.randint(0,10,10)\n",
    "print(np.intersect1d(Z1,Z2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 31. How to ignore all numpy warnings (not recommended)? (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Suicide mode on\n",
    "defaults = np.seterr(all=\"ignore\")\n",
    "Z = np.ones(1) / 0\n",
    "\n",
    "# Back to sanity\n",
    "_ = np.seterr(**defaults)\n",
    "\n",
    "An equivalent way, with a context manager:\n",
    "\n",
    "with np.errstate(divide='ignore'):\n",
    "    Z = np.ones(1) / 0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 32. Is the following expressions true? (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "np.sqrt(-1) == np.emath.sqrt(-1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')\n",
    "today     = np.datetime64('today', 'D')\n",
    "tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 34. How to get all the dates corresponding to the month of July 2016? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 35. How to compute ((A+B)\\*(-A/2)) in place (without copy)? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "A = np.ones(3)*1\n",
    "B = np.ones(3)*2\n",
    "C = np.ones(3)*3\n",
    "np.add(A,B,out=B)\n",
    "np.divide(A,2,out=A)\n",
    "np.negative(A,out=A)\n",
    "np.multiply(A,B,out=A)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 36. Extract the integer part of a random array using 5 different methods (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.uniform(0,10,10)\n",
    "\n",
    "print (Z - Z%1)\n",
    "print (np.floor(Z))\n",
    "print (np.ceil(Z)-1)\n",
    "print (Z.astype(int))\n",
    "print (np.trunc(Z))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.zeros((5,5))\n",
    "Z += np.arange(5)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def generate():\n",
    "    for x in range(10):\n",
    "        yield x\n",
    "Z = np.fromiter(generate(),dtype=float,count=-1)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.linspace(0,1,11,endpoint=False)[1:]\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 40. Create a random vector of size 10 and sort it (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.random(10)\n",
    "Z.sort()\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 41. How to sum a small array faster than np.sum? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Evgeni Burovski\n",
    "\n",
    "Z = np.arange(10)\n",
    "np.add.reduce(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 42. Consider two random array A and B, check if they are equal (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "A = np.random.randint(0,2,5)\n",
    "B = np.random.randint(0,2,5)\n",
    "\n",
    "# Assuming identical shape of the arrays and a tolerance for the comparison of values\n",
    "equal = np.allclose(A,B)\n",
    "print(equal)\n",
    "\n",
    "# Checking both the shape and the element values, no tolerance (values have to be exactly equal)\n",
    "equal = np.array_equal(A,B)\n",
    "print(equal)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 43. Make an array immutable (read-only) (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.zeros(10)\n",
    "Z.flags.writeable = False\n",
    "Z[0] = 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.random((10,2))\n",
    "X,Y = Z[:,0], Z[:,1]\n",
    "R = np.sqrt(X**2+Y**2)\n",
    "T = np.arctan2(Y,X)\n",
    "print(R)\n",
    "print(T)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.random(10)\n",
    "Z[Z.argmax()] = 0\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 46. Create a structured array with `x` and `y` coordinates covering the \\[0,1\\]x\\[0,1\\] area (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.zeros((5,5), [('x',float),('y',float)])\n",
    "Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5),\n",
    "                             np.linspace(0,1,5))\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "####  47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Evgeni Burovski\n",
    "\n",
    "X = np.arange(8)\n",
    "Y = X + 0.5\n",
    "C = 1.0 / np.subtract.outer(X, Y)\n",
    "print(np.linalg.det(C))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "for dtype in [np.int8, np.int32, np.int64]:\n",
    "   print(np.iinfo(dtype).min)\n",
    "   print(np.iinfo(dtype).max)\n",
    "for dtype in [np.float32, np.float64]:\n",
    "   print(np.finfo(dtype).min)\n",
    "   print(np.finfo(dtype).max)\n",
    "   print(np.finfo(dtype).eps)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 49. How to print all the values of an array? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "np.set_printoptions(threshold=np.nan)\n",
    "Z = np.zeros((16,16))\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 50. How to find the closest value (to a given scalar) in a vector? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.arange(100)\n",
    "v = np.random.uniform(0,100)\n",
    "index = (np.abs(Z-v)).argmin()\n",
    "print(Z[index])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.zeros(10, [ ('position', [ ('x', float, 1),\n",
    "                                  ('y', float, 1)]),\n",
    "                   ('color',    [ ('r', float, 1),\n",
    "                                  ('g', float, 1),\n",
    "                                  ('b', float, 1)])])\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.random((10,2))\n",
    "X,Y = np.atleast_2d(Z[:,0], Z[:,1])\n",
    "D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)\n",
    "print(D)\n",
    "\n",
    "# Much faster with scipy\n",
    "import scipy\n",
    "# Thanks Gavin Heverly-Coulson (#issue 1)\n",
    "import scipy.spatial\n",
    "\n",
    "Z = np.random.random((10,2))\n",
    "D = scipy.spatial.distance.cdist(Z,Z)\n",
    "print(D)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 53. How to convert a float (32 bits) array into an integer (32 bits) in place?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.arange(10, dtype=np.int32)\n",
    "Z = Z.astype(np.float32, copy=False)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 54. How to read the following file? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from io import StringIO\n",
    "\n",
    "# Fake file \n",
    "s = StringIO(\"\"\"1, 2, 3, 4, 5\\n\n",
    "                6,  ,  , 7, 8\\n\n",
    "                 ,  , 9,10,11\\n\"\"\")\n",
    "Z = np.genfromtxt(s, delimiter=\",\", dtype=np.int)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 55. What is the equivalent of enumerate for numpy arrays? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.arange(9).reshape(3,3)\n",
    "for index, value in np.ndenumerate(Z):\n",
    "    print(index, value)\n",
    "for index in np.ndindex(Z.shape):\n",
    "    print(index, Z[index])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 56. Generate a generic 2D Gaussian-like array (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))\n",
    "D = np.sqrt(X*X+Y*Y)\n",
    "sigma, mu = 1.0, 0.0\n",
    "G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )\n",
    "print(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 57. How to randomly place p elements in a 2D array? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Divakar\n",
    "\n",
    "n = 10\n",
    "p = 3\n",
    "Z = np.zeros((n,n))\n",
    "np.put(Z, np.random.choice(range(n*n), p, replace=False),1)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 58. Subtract the mean of each row of a matrix (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Warren Weckesser\n",
    "\n",
    "X = np.random.rand(5, 10)\n",
    "\n",
    "# Recent versions of numpy\n",
    "Y = X - X.mean(axis=1, keepdims=True)\n",
    "\n",
    "# Older versions of numpy\n",
    "Y = X - X.mean(axis=1).reshape(-1, 1)\n",
    "\n",
    "print(Y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 59. How to sort an array by the nth column? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Steve Tjoa\n",
    "\n",
    "Z = np.random.randint(0,10,(3,3))\n",
    "print(Z)\n",
    "print(Z[Z[:,1].argsort()])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 60. How to tell if a given 2D array has null columns? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Warren Weckesser\n",
    "\n",
    "Z = np.random.randint(0,3,(3,10))\n",
    "print((~Z.any(axis=0)).any())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 61. Find the nearest value from a given value in an array (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.uniform(0,1,10)\n",
    "z = 0.5\n",
    "m = Z.flat[np.abs(Z - z).argmin()]\n",
    "print(m)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "A = np.arange(3).reshape(3,1)\n",
    "B = np.arange(3).reshape(1,3)\n",
    "it = np.nditer([A,B,None])\n",
    "for x,y,z in it: z[...] = x + y\n",
    "print(it.operands[2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 63. Create an array class that has a name attribute (★★☆)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class NamedArray(np.ndarray):\n",
    "    def __new__(cls, array, name=\"no name\"):\n",
    "        obj = np.asarray(array).view(cls)\n",
    "        obj.name = name\n",
    "        return obj\n",
    "    def __array_finalize__(self, obj):\n",
    "        if obj is None: return\n",
    "        self.info = getattr(obj, 'name', \"no name\")\n",
    "\n",
    "Z = NamedArray(np.arange(10), \"range_10\")\n",
    "print (Z.name)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Brett Olsen\n",
    "\n",
    "Z = np.ones(10)\n",
    "I = np.random.randint(0,len(Z),20)\n",
    "Z += np.bincount(I, minlength=len(Z))\n",
    "print(Z)\n",
    "\n",
    "# Another solution\n",
    "# Author: Bartosz Telenczuk\n",
    "np.add.at(Z, I, 1)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Alan G Isaac\n",
    "\n",
    "X = [1,2,3,4,5,6]\n",
    "I = [1,3,9,3,4,1]\n",
    "F = np.bincount(I,X)\n",
    "print(F)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Nadav Horesh\n",
    "\n",
    "w,h = 16,16\n",
    "I = np.random.randint(0,2,(h,w,3)).astype(np.ubyte)\n",
    "#Note that we should compute 256*256 first. \n",
    "#Otherwise numpy will only promote F.dtype to 'uint16' and overfolw will occur\n",
    "F = I[...,0]*(256*256) + I[...,1]*256 +I[...,2]\n",
    "n = len(np.unique(F))\n",
    "print(n)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "A = np.random.randint(0,10,(3,4,3,4))\n",
    "# solution by passing a tuple of axes (introduced in numpy 1.7.0)\n",
    "sum = A.sum(axis=(-2,-1))\n",
    "print(sum)\n",
    "# solution by flattening the last two dimensions into one\n",
    "# (useful for functions that don't accept tuples for axis argument)\n",
    "sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)\n",
    "print(sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset  indices? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Jaime Fernández del Río\n",
    "\n",
    "D = np.random.uniform(0,1,100)\n",
    "S = np.random.randint(0,10,100)\n",
    "D_sums = np.bincount(S, weights=D)\n",
    "D_counts = np.bincount(S)\n",
    "D_means = D_sums / D_counts\n",
    "print(D_means)\n",
    "\n",
    "# Pandas solution as a reference due to more intuitive code\n",
    "import pandas as pd\n",
    "print(pd.Series(D).groupby(S).mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 69. How to get the diagonal of a dot product? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Mathieu Blondel\n",
    "\n",
    "A = np.random.uniform(0,1,(5,5))\n",
    "B = np.random.uniform(0,1,(5,5))\n",
    "\n",
    "# Slow version  \n",
    "np.diag(np.dot(A, B))\n",
    "\n",
    "# Fast version\n",
    "np.sum(A * B.T, axis=1)\n",
    "\n",
    "# Faster version\n",
    "np.einsum(\"ij,ji->i\", A, B)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 70. Consider the vector \\[1, 2, 3, 4, 5\\], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Warren Weckesser\n",
    "\n",
    "Z = np.array([1,2,3,4,5])\n",
    "nz = 3\n",
    "Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))\n",
    "Z0[::nz+1] = Z\n",
    "print(Z0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "A = np.ones((5,5,3))\n",
    "B = 2*np.ones((5,5))\n",
    "print(A * B[:,:,None])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 72. How to swap two rows of an array? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Eelco Hoogendoorn\n",
    "\n",
    "A = np.arange(25).reshape(5,5)\n",
    "A[[0,1]] = A[[1,0]]\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the  triangles (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Nicolas P. Rougier\n",
    "\n",
    "faces = np.random.randint(0,100,(10,3))\n",
    "F = np.roll(faces.repeat(2,axis=1),-1,axis=1)\n",
    "F = F.reshape(len(F)*3,2)\n",
    "F = np.sort(F,axis=1)\n",
    "G = F.view( dtype=[('p0',F.dtype),('p1',F.dtype)] )\n",
    "G = np.unique(G)\n",
    "print(G)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 74. Given an array C that is a bincount, how to produce an array A such that np.bincount(A) == C? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Jaime Fernández del Río\n",
    "\n",
    "C = np.bincount([1,1,2,3,4,4,6])\n",
    "A = np.repeat(np.arange(len(C)), C)\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 75. How to compute averages using a sliding window over an array? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Jaime Fernández del Río\n",
    "\n",
    "def moving_average(a, n=3) :\n",
    "    ret = np.cumsum(a, dtype=float)\n",
    "    ret[n:] = ret[n:] - ret[:-n]\n",
    "    return ret[n - 1:] / n\n",
    "Z = np.arange(20)\n",
    "print(moving_average(Z, n=3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z\\[0\\],Z\\[1\\],Z\\[2\\]) and each subsequent row is  shifted by 1 (last row should be (Z\\[-3\\],Z\\[-2\\],Z\\[-1\\]) (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Joe Kington / Erik Rigtorp\n",
    "from numpy.lib import stride_tricks\n",
    "\n",
    "def rolling(a, window):\n",
    "    shape = (a.size - window + 1, window)\n",
    "    strides = (a.itemsize, a.itemsize)\n",
    "    return stride_tricks.as_strided(a, shape=shape, strides=strides)\n",
    "Z = rolling(np.arange(10), 3)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 77. How to negate a boolean, or to change the sign of a float inplace? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Nathaniel J. Smith\n",
    "\n",
    "Z = np.random.randint(0,2,100)\n",
    "np.logical_not(Z, out=Z)\n",
    "\n",
    "Z = np.random.uniform(-1.0,1.0,100)\n",
    "np.negative(Z, out=Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 78. Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i  (P0\\[i\\],P1\\[i\\])? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def distance(P0, P1, p):\n",
    "    T = P1 - P0\n",
    "    L = (T**2).sum(axis=1)\n",
    "    U = -((P0[:,0]-p[...,0])*T[:,0] + (P0[:,1]-p[...,1])*T[:,1]) / L\n",
    "    U = U.reshape(len(U),1)\n",
    "    D = P0 + U*T - p\n",
    "    return np.sqrt((D**2).sum(axis=1))\n",
    "\n",
    "P0 = np.random.uniform(-10,10,(10,2))\n",
    "P1 = np.random.uniform(-10,10,(10,2))\n",
    "p  = np.random.uniform(-10,10,( 1,2))\n",
    "print(distance(P0, P1, p))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 79. Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j (P\\[j\\]) to each line i (P0\\[i\\],P1\\[i\\])? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Italmassov Kuanysh\n",
    "\n",
    "# based on distance function from previous question\n",
    "P0 = np.random.uniform(-10, 10, (10,2))\n",
    "P1 = np.random.uniform(-10,10,(10,2))\n",
    "p = np.random.uniform(-10, 10, (10,2))\n",
    "print(np.array([distance(P0,P1,p_i) for p_i in p]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 80. Consider an arbitrary array, write a function that extract a subpart with a fixed shape and centered on a given element (pad with a `fill` value when necessary) (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Nicolas Rougier\n",
    "\n",
    "Z = np.random.randint(0,10,(10,10))\n",
    "shape = (5,5)\n",
    "fill  = 0\n",
    "position = (1,1)\n",
    "\n",
    "R = np.ones(shape, dtype=Z.dtype)*fill\n",
    "P  = np.array(list(position)).astype(int)\n",
    "Rs = np.array(list(R.shape)).astype(int)\n",
    "Zs = np.array(list(Z.shape)).astype(int)\n",
    "\n",
    "R_start = np.zeros((len(shape),)).astype(int)\n",
    "R_stop  = np.array(list(shape)).astype(int)\n",
    "Z_start = (P-Rs//2)\n",
    "Z_stop  = (P+Rs//2)+Rs%2\n",
    "\n",
    "R_start = (R_start - np.minimum(Z_start,0)).tolist()\n",
    "Z_start = (np.maximum(Z_start,0)).tolist()\n",
    "R_stop = np.maximum(R_start, (R_stop - np.maximum(Z_stop-Zs,0))).tolist()\n",
    "Z_stop = (np.minimum(Z_stop,Zs)).tolist()\n",
    "\n",
    "r = [slice(start,stop) for start,stop in zip(R_start,R_stop)]\n",
    "z = [slice(start,stop) for start,stop in zip(Z_start,Z_stop)]\n",
    "R[r] = Z[z]\n",
    "print(Z)\n",
    "print(R)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 81. Consider an array Z = \\[1,2,3,4,5,6,7,8,9,10,11,12,13,14\\], how to generate an array R = \\[\\[1,2,3,4\\], \\[2,3,4,5\\], \\[3,4,5,6\\], ..., \\[11,12,13,14\\]\\]? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Stefan van der Walt\n",
    "\n",
    "Z = np.arange(1,15,dtype=np.uint32)\n",
    "R = stride_tricks.as_strided(Z,(11,4),(4,4))\n",
    "print(R)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 82. Compute a matrix rank (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Stefan van der Walt\n",
    "\n",
    "Z = np.random.uniform(0,1,(10,10))\n",
    "U, S, V = np.linalg.svd(Z) # Singular Value Decomposition\n",
    "rank = np.sum(S > 1e-10)\n",
    "print(rank)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 83. How to find the most frequent value in an array?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.random.randint(0,10,50)\n",
    "print(np.bincount(Z).argmax())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 84. Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Chris Barker\n",
    "\n",
    "Z = np.random.randint(0,5,(10,10))\n",
    "n = 3\n",
    "i = 1 + (Z.shape[0]-3)\n",
    "j = 1 + (Z.shape[1]-3)\n",
    "C = stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)\n",
    "print(C)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 85. Create a 2D array subclass such that Z\\[i,j\\] == Z\\[j,i\\] (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Eric O. Lebigot\n",
    "# Note: only works for 2d array and value setting using indices\n",
    "\n",
    "class Symetric(np.ndarray):\n",
    "    def __setitem__(self, index, value):\n",
    "        i,j = index\n",
    "        super(Symetric, self).__setitem__((i,j), value)\n",
    "        super(Symetric, self).__setitem__((j,i), value)\n",
    "\n",
    "def symetric(Z):\n",
    "    return np.asarray(Z + Z.T - np.diag(Z.diagonal())).view(Symetric)\n",
    "\n",
    "S = symetric(np.random.randint(0,10,(5,5)))\n",
    "S[2,3] = 42\n",
    "print(S)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 86. Consider a set of p matrices wich shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of of the p matrix products at once? (result has shape (n,1)) (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Stefan van der Walt\n",
    "\n",
    "p, n = 10, 20\n",
    "M = np.ones((p,n,n))\n",
    "V = np.ones((p,n,1))\n",
    "S = np.tensordot(M, V, axes=[[0, 2], [0, 1]])\n",
    "print(S)\n",
    "\n",
    "# It works, because:\n",
    "# M is (p,n,n)\n",
    "# V is (p,n,1)\n",
    "# Thus, summing over the paired axes 0 and 0 (of M and V independently),\n",
    "# and 2 and 1, to remain with a (n,1) vector."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 87. Consider a 16x16 array, how to get the block-sum (block size is 4x4)? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Robert Kern\n",
    "\n",
    "Z = np.ones((16,16))\n",
    "k = 4\n",
    "S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),\n",
    "                                       np.arange(0, Z.shape[1], k), axis=1)\n",
    "print(S)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 88. How to implement the Game of Life using numpy arrays? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Nicolas Rougier\n",
    "\n",
    "def iterate(Z):\n",
    "    # Count neighbours\n",
    "    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +\n",
    "         Z[1:-1,0:-2]                + Z[1:-1,2:] +\n",
    "         Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])\n",
    "\n",
    "    # Apply rules\n",
    "    birth = (N==3) & (Z[1:-1,1:-1]==0)\n",
    "    survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)\n",
    "    Z[...] = 0\n",
    "    Z[1:-1,1:-1][birth | survive] = 1\n",
    "    return Z\n",
    "\n",
    "Z = np.random.randint(0,2,(50,50))\n",
    "for i in range(100): Z = iterate(Z)\n",
    "print(Z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 89. How to get the n largest values of an array (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.arange(10000)\n",
    "np.random.shuffle(Z)\n",
    "n = 5\n",
    "\n",
    "# Slow\n",
    "print (Z[np.argsort(Z)[-n:]])\n",
    "\n",
    "# Fast\n",
    "print (Z[np.argpartition(-Z,n)[:n]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 90. Given an arbitrary number of vectors, build the cartesian product (every combinations of every item) (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Author: Stefan Van der Walt\n",
    "\n",
    "def cartesian(arrays):\n",
    "    arrays = [np.asarray(a) for a in arrays]\n",
    "    shape = (len(x) for x in arrays)\n",
    "\n",
    "    ix = np.indices(shape, dtype=int)\n",
    "    ix = ix.reshape(len(arrays), -1).T\n",
    "\n",
    "    for n, arr in enumerate(arrays):\n",
    "        ix[:, n] = arrays[n][ix[:, n]]\n",
    "\n",
    "    return ix\n",
    "\n",
    "print (cartesian(([1, 2, 3], [4, 5], [6, 7])))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 91. How to create a record array from a regular array? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Z = np.array([(\"Hello\", 2.5, 3),\n",
    "              (\"World\", 3.6, 2)])\n",
    "R = np.core.records.fromarrays(Z.T, \n",
    "                               names='col1, col2, col3',\n",
    "                               formats = 'S8, f8, i8')\n",
    "print(R)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 92. Consider a large vector Z, compute Z to the power of 3 using 3 different methods (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Ryan G.\n",
    "\n",
    "x = np.random.rand(5e7)\n",
    "\n",
    "%timeit np.power(x,3)\n",
    "%timeit x*x*x\n",
    "%timeit np.einsum('i,i,i->i',x,x,x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 93. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain elements of each row of B regardless of the order of the elements in B? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Gabe Schwartz\n",
    "\n",
    "A = np.random.randint(0,5,(8,3))\n",
    "B = np.random.randint(0,5,(2,2))\n",
    "\n",
    "C = (A[..., np.newaxis, np.newaxis] == B)\n",
    "rows = np.where(C.any((3,1)).all(1))[0]\n",
    "print(rows)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 94. Considering a 10x3 matrix, extract rows with unequal values (e.g. \\[2,2,3\\]) (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Robert Kern\n",
    "\n",
    "Z = np.random.randint(0,5,(10,3))\n",
    "print(Z)\n",
    "# solution for arrays of all dtypes (including string arrays and record arrays)\n",
    "E = np.all(Z[:,1:] == Z[:,:-1], axis=1)\n",
    "U = Z[~E]\n",
    "print(U)\n",
    "# soluiton for numerical arrays only, will work for any number of columns in Z\n",
    "U = Z[Z.max(axis=1) != Z.min(axis=1),:]\n",
    "print(U)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 95. Convert a vector of ints into a matrix binary representation (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Warren Weckesser\n",
    "\n",
    "I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128])\n",
    "B = ((I.reshape(-1,1) & (2**np.arange(8))) != 0).astype(int)\n",
    "print(B[:,::-1])\n",
    "\n",
    "# Author: Daniel T. McDonald\n",
    "\n",
    "I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128], dtype=np.uint8)\n",
    "print(np.unpackbits(I[:, np.newaxis], axis=1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 96. Given a two dimensional array, how to extract unique rows? (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Jaime Fernández del Río\n",
    "\n",
    "Z = np.random.randint(0,2,(6,3))\n",
    "T = np.ascontiguousarray(Z).view(np.dtype((np.void, Z.dtype.itemsize * Z.shape[1])))\n",
    "_, idx = np.unique(T, return_index=True)\n",
    "uZ = Z[idx]\n",
    "print(uZ)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 97. Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "A = np.random.uniform(0,1,10)\n",
    "B = np.random.uniform(0,1,10)\n",
    "\n",
    "np.einsum('i->', A)       # np.sum(A)\n",
    "np.einsum('i,i->i', A, B) # A * B\n",
    "np.einsum('i,i', A, B)    # np.inner(A, B)\n",
    "np.einsum('i,j->ij', A, B)    # np.outer(A, B)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 98. Considering a path described by two vectors (X,Y), how to sample it using equidistant samples (★★★)?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Bas Swinckels\n",
    "\n",
    "phi = np.arange(0, 10*np.pi, 0.1)\n",
    "a = 1\n",
    "x = a*phi*np.cos(phi)\n",
    "y = a*phi*np.sin(phi)\n",
    "\n",
    "dr = (np.diff(x)**2 + np.diff(y)**2)**.5 # segment lengths\n",
    "r = np.zeros_like(x)\n",
    "r[1:] = np.cumsum(dr)                # integrate path\n",
    "r_int = np.linspace(0, r.max(), 200) # regular spaced path\n",
    "x_int = np.interp(r_int, r, x)       # integrate path\n",
    "y_int = np.interp(r_int, r, y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 99. Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees, i.e., the rows which only contain integers and which sum to n. (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Evgeni Burovski\n",
    "\n",
    "X = np.asarray([[1.0, 0.0, 3.0, 8.0],\n",
    "                [2.0, 0.0, 1.0, 1.0],\n",
    "                [1.5, 2.5, 1.0, 0.0]])\n",
    "n = 4\n",
    "M = np.logical_and.reduce(np.mod(X, 1) == 0, axis=-1)\n",
    "M &= (X.sum(axis=-1) == n)\n",
    "print(X[M])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 100. Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (i.e., resample the elements of an array with replacement N times, compute the mean of each sample, and then compute percentiles over the means). (★★★)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Author: Jessica B. Hamrick\n",
    "\n",
    "X = np.random.randn(100) # random 1D array\n",
    "N = 1000 # number of bootstrap samples\n",
    "idx = np.random.randint(0, X.size, (N, X.size))\n",
    "means = X[idx].mean(axis=1)\n",
    "confint = np.percentile(means, [2.5, 97.5])\n",
    "print(confint)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
