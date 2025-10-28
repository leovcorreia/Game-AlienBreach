package com.alien_breach.demo.controllers;

import com.alien_breach.demo.services.GameService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/game")
public class GameController {

    @Autowired
    private GameService gameService;

    @PostMapping("/start")
    public start() {

    }

    @PostMapping("/event/energizer")
    public eventEnergizer() {

    }

    @PostMapping("/event/bonus")
    public eventBonus() {

    }

    @PostMapping("/event/life-lost")
    public eventLifeLost() {

    }

    @PostMapping("/event/pellets")
    public eventPellets() {

    }

    @PostMapping("/level-up")
    public eventLevelUp() {

    }

    @PostMapping("/state")
    public state() {

    }

    @PostMapping("/over")
    public gameOver() {

    }

}
