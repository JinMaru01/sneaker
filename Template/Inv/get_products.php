<?php
// Establish a database connection (replace with your own credentials)
$host = 'localhost';
$username = 'root';
$password = '';
$database = 'capstone';

$conn = new mysqli($host, $username, $password, $database);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Fetch products from the database
$query = "SELECT * FROM products";
$result = $conn->query($query);

// Create an empty array to store the products
$products = [];

if ($result->num_rows > 0) {
    // Loop through the result and fetch each product as an associative array
    while ($row = $result->fetch_assoc()) {
        $product = [
            'id' => $row['id'],
            'name' => $row['name'],
            'image' => $row['image'],
            'price' => $row['price']
        ];

        // Add the product to the products array
        $products[] = $product;
    }
}

// Close the database connection
$conn->close();

// Convert the products array to JSON and echo it as the response
header('Content-Type: application/json');
echo json_encode($products);
?>
