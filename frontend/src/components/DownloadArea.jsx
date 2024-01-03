import { useRef, useState } from "react";

import youtube_parser from "./utils/Utils";
import axios from "axios";
import ReactPlayer from "react-player";

export default () => {
    // Coleta o link do youtube
    const inputUrlRef = useRef();

    const [ytUrl, setYtUrl] = useState(null);

    // recebe o envio do formulario com o link
    const handleSubmit = (e) => {
        e.preventDefault();
        const ytID = youtube_parser(inputUrlRef.current.value);

        const options = {
            method: "GET",
            url: "https://youtube-mp36.p.rapidapi.com/dl",
            params: { id: "UxxajLWwzqY" },
            headers: {
                "X-RapidAPI-Key": import.meta.env.VITE_RAPID_API_KEY,
                "X-RapidAPI-Host": "youtube-mp36.p.rapidapi.com"
            },
            params: {
                id: ytID
            }
        };

        axios(options)
            .then((res) => setYtUrl(res.data.link))
            .catch((err) => console.log(err));

        inputUrlRef.current.value = "";
    };

    return (
        <>
            {/*Seção principal para donwload*/}
            <section className="bg-yt">
                <div className="p-5 container text-center">
                    <div className="d-flex justify-content-center">
                        <h1 className="me-2 pt-1">Insira um link e baixe</h1>
                        <h1 className="display-4 fs-bowb color-primary txt-deco no-under">
                            qualquer tipo de vídeo!
                        </h1>
                    </div>
                    <form className="row" onSubmit={handleSubmit}>
                        <div className="pt-5 pb-3">
                            <input
                                ref={inputUrlRef}
                                type="text"
                                className="form-control form-control-lg col-md-6 shadow"
                                placeholder="link..."
                                required
                            />
                            <button
                                type="submit"
                                className="btn btn-lg btn-primary col-md-6 mt-3"
                            >
                                enviar
                            </button>
                        </div>
                    </form>
                </div>
            </section>
            {ytUrl ? (
                <section className="container text-center">
                    <h1 className="pb-5">
                        Coloque o link e veja se este e o seu vídeo
                    </h1>
                    <div className="d-flex justify-content-center">
                        <ReactPlayer
                            url="https://www.youtube.com/watch?v=PRfMwXCs3S8&t=487s"
                            controls
                        />
                    </div>
                    <div>
                        <a
                            target="_blank"
                            rel="noreferrer"
                            href={ytUrl}
                            className="btn btn-light"
                        >
                            Baixe versão mp3
                        </a>
                    </div>
                </section>
            ) : (
                ""
            )}
        </>
    );
};
