# Fakeinfo API

This is a Python API built with Flask that provides fake information for testing and development purposes. It offers endpoints to retrieve and manipulate fake posts, comments, users, jobs, and generate image placeholders.
## Options
There are two options, you can install this project and run it locally, or use access it online at https://fakeinfo.info. You'll find how to the online API. If you want to run it locally, you can continue to the installation and usage guides.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your/repo.git
   ```

2. Change to the project directory:

   ```bash
   cd repo
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the API, run the following command:

```bash
python app.py
```

The API will start running on `http://localhost:5000/`.

## Endpoints

### Home

- `GET /api`
- `GET /api/v1`

Returns a welcome message and the status of the API.

### Posts

- `GET /api/v1/posts`
- `GET /api/v1/posts/paginate`
- `GET /api/v1/post/<int:id>`

Retrieves posts, paginated posts, or a single post by its ID.

### Comments

- `GET /api/v1/comments`
- `GET /api/v1/comments/paginate`
- `GET /api/v1/comment/<int:id>`

Retrieves comments, paginated comments, or a single comment by its ID.

### Users

- `GET /api/v1/users`
- `GET /api/v1/users/paginate`
- `GET /api/v1/user/<int:id>`

Retrieves users, paginated users, or a single user by their ID.

### Jobs

- `GET /api/v1/jobs`
- `GET /api/v1/jobs/paginate`
- `GET /api/v1/job/<int:id>`

Retrieves jobs, paginated jobs, or a single job by its ID.

### Image Placeholder

- `GET /api/v1/imageplaceholder`

Generates a placeholder image with 400x200 dimensions.

- `GET /api/v1/imageplaceholder?width=<width>&height=<height>`
Generates a placeholder image with specified dimensions. Default: 400x200

## Error Handling

If any error occurs during the API request processing, a JSON response with the following structure will be returned:

```json
{
  "status": "failed",
  "message": "Error message"
}
```

The error message will provide details about the encountered issue.

## Contributing
Contributions to the Fakeinfo API are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request.

## Disclaimer

This API is intended for testing and development purposes only. The data provided is randomly generated and should not be used for any real-world scenarios.

## License

The Fakeinfo API is released under the [MIT License](./LICENSE). Feel free to modify and use it as needed.