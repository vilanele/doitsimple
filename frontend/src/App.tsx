import Button from "@mui/material/Button";
import { styled } from '@mui/material/styles';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import axios from "axios";

const VisuallyHiddenInput = styled('input')({
	clip: 'rect(0 0 0 0)',
	clipPath: 'inset(50%)',
	height: 1,
	overflow: 'hidden',
	position: 'absolute',
	bottom: 0,
	left: 0,
	whiteSpace: 'nowrap',
	width: 1,
});

function App() {

	async function onUpload(event: React.ChangeEvent<HTMLInputElement>) {
		const formData = new FormData()
		formData.append("file", event.target.files[0])
		await axios.post("http://localhost:9000/ogg-to-mp3/", formData, {
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		})
	}


	return (
		<>
			<Button
				component="label"
				role={undefined}
				variant="contained"
				tabIndex={-1}
				startIcon={<CloudUploadIcon />}
			>
				Upload files
				<VisuallyHiddenInput
					type="file"
					onChange={onUpload}
					multiple
				/>
			</Button>
		</>
	)
}

export default App
